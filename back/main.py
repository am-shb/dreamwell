# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from openai import OpenAI
from typing import List, Optional
import asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

aiclient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class BrandRequest(BaseModel):
    name: str
    description: str
    brandValues: List[str]
    campaignGoal: str
    brandVoice: str
    dealbreakers: List[str]
    minSubs: int = 10000
    minVideoViews: int = 50000
    maxResults: int = 10

class ChannelResult(BaseModel):
    id: str
    title: str
    thumbnail: str
    cover_photo: str
    subs: int
    avg_views: int
    engagement_rate: float
    video_count: int
    description: str
    match_reason: str

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
async def youtube_api_call(url: str, params: dict):
    print(f"\n📡 YouTube API call to {url} ...")
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(url, params=params)
        print(f"✅ YouTube API response: {response.status_code}")
        return response.json()

async def get_video_details(video_ids: List[str]):
    print(f"\n🔍 Fetching details for {len(video_ids)} videos")
    params = {
        "part": "snippet,statistics",
        "id": ",".join(video_ids),
        "key": os.getenv("YOUTUBE_API_KEY")
    }
    data = await youtube_api_call("https://www.googleapis.com/youtube/v3/videos", params)
    print(f"📊 Got stats for {len(data.get('items', []))} videos")
    return {item["id"]: item for item in data.get("items", [])}

async def get_popular_channels(brand: BrandRequest, search_terms: List[str]):
    print(f"\n🔎 Starting video search with terms: {search_terms}")
    all_videos = []
    
    async with httpx.AsyncClient() as client:
        for term in search_terms:
            print(f"\n🕵️ Searching videos for: '{term}'")
            params = {
                "part": "snippet",
                "q": term,
                "type": "video",
                "order": "viewCount",
                "maxResults": 2,
                "key": os.getenv("YOUTUBE_API_KEY")
            }
            search_data = await youtube_api_call(
                "https://www.googleapis.com/youtube/v3/search",
                params
            )
            new_videos = search_data.get("items", [])
            print(f"🎥 Found {len(new_videos)} videos for '{term}'")
            all_videos.extend(new_videos)
    
    print(f"\n📦 Total videos collected: {len(all_videos)}")
    
    # Batch process video statistics
    # video_ids = [v["id"]["videoId"] for v in all_videos]
    # video_details = await get_video_details(video_ids)
    
    # Filter videos by view count
    filtered_videos = all_videos
    # filtered_videos = []
    # for v in all_videos:
    #     vid = v["id"]["videoId"]
    #     views = int(video_details.get(vid, {}).get("statistics", {}).get("viewCount", 0))
    #     if views >= brand.minVideoViews:
    #         filtered_videos.append(v)
    # print(f"🎯 High-view videos (>={brand.minVideoViews} views): {len(filtered_videos)}")
    
    # Get unique channels from popular videos
    channel_ids = list({v["snippet"]["channelId"] for v in filtered_videos})
    print(f"👥 Unique channels found: {len(channel_ids)}")
    
    # Get channel details
    print("\n📡 Fetching channel details...")
    params = {
        "part": "snippet,statistics,brandingSettings",
        "id": ",".join(channel_ids),
        "key": os.getenv("YOUTUBE_API_KEY")
    }
    channels_data = await youtube_api_call(
        "https://www.googleapis.com/youtube/v3/channels",
        params
    )
    
    valid_channels = []
    for c in channels_data.get("items", []):
        subs = int(c["statistics"]["subscriberCount"])
        if subs >= brand.minSubs:
            valid_channels.append(c)
            print(f"📈 Valid channel: {c['snippet']['title']} ({subs} subs)")
        else:
            print(f"⏬ Rejected: {c['snippet']['title']} ({subs} < {brand.minSubs})")
    
    print(f"\n🏆 Qualified channels: {len(valid_channels)}")
    
    return [
        {
            "id": c["id"],
            "title": c["snippet"]["title"],
            "description": c["snippet"]["description"],
            "subs": int(c["statistics"]["subscriberCount"]),
            "views": int(c["statistics"]["viewCount"]),
            "videos": int(c["statistics"]["videoCount"]),
            "thumbnail": c["snippet"]["thumbnails"]["high"]["url"],
            "cover_photo": c["brandingSettings"].get("image", {"bannerExternalUrl": ""}).get("bannerExternalUrl", ""),
            # "top_video_views": max(
            #     int(video_details[v["id"]["videoId"]]["statistics"]["viewCount"])
            #     for v in filtered_videos if v["snippet"]["channelId"] == c["id"]
            # )
        }
        for c in valid_channels
    ]

async def analyze_channel(brand: BrandRequest, channel: dict) -> Optional[ChannelResult]:
    print(f"\n🔬 Analyzing {channel['title']} ({channel['subs']} subs)")
    
    class BrandOutput(BaseModel):
        reason: str
        decision: bool
    try:
        completion = aiclient.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a brand looking to collaborate with influencers. Analyze the channel and brand given by the user and return a reseaoning whther the two should collaborate."},
                {"role": "user", "content": 
                    f"""Channel info
                    Channel name: {channel['title']}
                    Subscribers: {channel['subs']}
                    Views: {channel['views']}
                    Videos: {channel['videos']}
                    Description: {channel['description']}
                    
                    Brand info
                    Name: {brand.name}
                    Description: {brand.description}
                    Values: {", ".join(brand.brandValues)}
                    Campaign goal: {brand.campaignGoal}
                    Brand voice: {brand.brandVoice}
                    Dealbreakers: {", ".join(brand.dealbreakers)}
                    """},
            ],
            response_format=BrandOutput,
        )

        alignment = completion.choices[0].message.parsed
        decision = alignment.decision
        reason = alignment.reason
        
        if not decision:
            print(f"❌ Rejected: {reason}")
            return None
        print(f"✅ Approved: {reason}")
    except Exception as e:
        print(f"⚠️ AI check failed: {str(e)}")
        return None


    # Calculate metrics
    avg_views = channel['views'] // max(channel['videos'], 1)
    engagement = (avg_views / max(channel['subs'], 1)) * 100

    return ChannelResult(
        id=channel["id"],
        title=channel["title"],
        thumbnail=channel["thumbnail"],
        cover_photo=channel["cover_photo"],
        subs=channel["subs"],
        avg_views=avg_views,
        engagement_rate=round(engagement, 1),
        video_count=channel["videos"],
        description=channel["description"][:200] + "...",
        match_reason=alignment.reason
    )

async def get_search_terms(brand: BrandRequest):
    print("\n🧠 Generating AI search terms...")
    search_terms = aiclient.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{
            "role": "user",
            "content": f"""
            You are a brand looking for influencers to collaborate with.
            Here are info about your brand:
            Name: {brand.name}
            Description: {brand.description}
            values: {", ".join(brand.brandValues)}
            campaign goal: {brand.campaignGoal}
            brand voice: {brand.brandVoice}
            dealbreakers: {", ".join(brand.dealbreakers)}
            
            Generate 3 search terms for finding influencers whose audiencd aligns with your brand.
            Remember you are searching for videos. use terms that finds videos that align with your target audience.
            output a comma seperated list of search terms only.
        """
        }]
    ).choices[0].message.content.strip().split(",")[:3]
    print(f"🔍 AI-generated search terms: {search_terms}")
    return search_terms

@app.post("/find-influencers", response_model=List[ChannelResult])
async def find_influencers(brand: BrandRequest):
    print("\n" + "="*50)
    print(f"🚀 STARTING NEW SEARCH: {brand.name}")
    print(f"🎯 Target: {brand.description}")
    print(f"⭐ Values: {brand.brandValues}")
    print(f"🚫 Dealbreakers: {brand.dealbreakers}")
    print("="*50)
    
    try:
        # Generate search terms
        search_terms = await get_search_terms(brand)
        
        # Find channels through popular videos
        channels = await get_popular_channels(brand, search_terms)
        
        # Analyze channels
        print(f"\n🔎 Analyzing {len(channels)} qualified channels")
        analysis_tasks = [analyze_channel(brand, c) for c in channels]
        results = await asyncio.gather(*analysis_tasks)
        
        # Final processing
        valid_results = [r for r in results if r is not None]
        # valid_results.sort(key=lambda x: x.top_video_views, reverse=True)
        
        print("\n" + "="*50)
        print(f"🏁 SEARCH COMPLETE! Found {len(valid_results)} matching influencers")
        # print(f"🏆 Top video views: {valid_results[0].top_video_views if valid_results else 0}")
        print("="*50)
        
        return valid_results[:brand.maxResults]
    
    except Exception as e:
        print("\n🔥 CRITICAL ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("\n⚡ Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)