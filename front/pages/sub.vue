<template>
    <div class="py-6">
      <div class="mb-8">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between">
          <div>
            <h1 class="text-2xl font-bold text-gray-900 sm:text-3xl">YouTube Influencers</h1>
            <p class="mt-2 text-sm text-gray-600">
              Browse and discover potential YouTube influencers for your campaigns
            </p>
          </div>
          <div class="mt-4 md:mt-0">
            <div class="flex space-x-3">
              <div class="relative">
                <input
                  type="text"
                  placeholder="Search influencers..."
                  v-model="searchQuery"
                  class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:ring-purple-500 focus:border-purple-500"
                />
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Search class="h-5 w-5 text-gray-400" />
                </div>
              </div>
              <button class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-purple-600 hover:bg-purple-700 focus:outline-none">
                <Filter class="h-4 w-4 mr-2" />
                Filter
              </button>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Grid of influencer cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="(influencer, index) in filteredInfluencers" :key="index" 
             class="bg-white rounded-lg shadow overflow-hidden hover:shadow-md transition-shadow duration-300">
          <!-- Card header with thumbnail -->
          <div class="relative">
            <img :src="influencer.coverImage" alt="Channel cover" class="w-full h-32 object-cover" />
            <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-4">
              <h3 class="text-white font-bold text-lg">{{ influencer.title }}</h3>
            </div>
            <div class="absolute top-4 right-4">
              <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">
                <Youtube class="h-3 w-3 mr-1" />
                YouTube
              </span>
            </div>
          </div>
          
          <!-- Card content -->
          <div class="p-4">
            <div class="flex items-start mb-4">
              <img :src="influencer.thumbnail" alt="Channel avatar" class="w-12 h-12 rounded-full mr-3 border-2 border-white shadow-sm" />
              <div>
                <!-- <div class="flex flex-wrap gap-2">
                  <span v-for="(category, catIndex) in influencer.categories" :key="catIndex"
                        class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800">
                    {{ category }}
                  </span>
                </div> -->
                <div class="flex items-center mt-1 text-sm text-gray-500">
                  <Users class="h-4 w-4 mr-1" />
                  {{ formatNumber(influencer.subs) }} subscribers
                </div>
              </div>
            </div>
            
            <!-- Description paragraph -->
            <p class="text-sm text-gray-600 mb-4">
              {{ influencer.description }}
            </p>

            <hr>

            <!-- Match reason -->
            <div class="mt-4">
              <h4 class="text-sm font-medium text-gray-900">Match Reason</h4>
              <p class="text-sm text-gray-600">{{ influencer.match_reason }}</p>
            </div>
            
            <!-- Stats -->
            <div class="grid grid-cols-3 gap-2 mb-4 text-center">
              <div class="bg-gray-50 rounded p-2">
                <div class="text-sm font-medium text-gray-900">{{ formatNumber(influencer.avg_views) }}</div>
                <div class="text-xs text-gray-500">Avg. Views</div>
              </div>
              <div class="bg-gray-50 rounded p-2">
                <div class="text-sm font-medium text-gray-900">{{ influencer.engagement_rate }}%</div>
                <div class="text-xs text-gray-500">Engagement</div>
              </div>
              <div class="bg-gray-50 rounded p-2">
                <div class="text-sm font-medium text-gray-900">{{ influencer.video_count }}</div>
                <div class="text-xs text-gray-500">Videos</div>
              </div>
            </div>
            
            <!-- Actions -->
            <div class="flex justify-between">
              <button class="inline-flex items-center px-3 py-1.5 border border-gray-300 text-sm font-medium rounded text-gray-700 bg-white hover:bg-gray-50">
                <Info class="h-4 w-4 mr-1" />
                Details
              </button>
              <button class="inline-flex items-center px-3 py-1.5 border border-transparent text-sm font-medium rounded text-white bg-purple-600 hover:bg-purple-700">
                <Plus class="h-4 w-4 mr-1" />
                Add to Campaign
              </button>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Empty state -->
      <div v-if="filteredInfluencers.length === 0" class="text-center py-12 bg-white rounded-lg shadow">
        <SearchX class="mx-auto h-12 w-12 text-gray-400" />
        <h3 class="mt-2 text-lg font-medium text-gray-900">No influencers found</h3>
        <p class="mt-1 text-sm text-gray-500">Try adjusting your search or filters to find what you're looking for.</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import { 
    Search, 
    Filter, 
    Users, 
    Info, 
    Plus,
    Youtube,
    SearchX
  } from 'lucide-vue-next';
  
  const searchQuery = ref('');
  
  const influencers = ref([
    {
        "id": "UCNAf1k0yIjyGu3k9BwAg3lg",
        "title": "Sky Sports Premier League",
        "thumbnail": "https://yt3.ggpht.com/LD8242zKW9zIrG1bp7yBCt7qQbzuPahSTJDaU9W_5GpG_JUaMx6HNbNjHdM4O-Q3Qv2xpWORJg=s800-c-k-c0x00ffffff-no-rj",
        "subs": 5440000,
        "avg_views": 363099,
        "engagement_rate": 6.7,
        "video_count": 12815,
        "description": "Sky Sports Premier League is the home of Sky Sports' Premier League videos on YouTube featuring highlights from every game of the season, as well as post match interviews, exclusive player access and top level analysis!\n\nMake sure you subscribe and turn on notifications so you don't miss a single upload!",
        "match_reason": "Sky Sports Premier League is a good match for the brand's awareness goal as it has a large, dedicated viewership of sports enthusiasts who value sustainability and ethical production, and its professional voice aligns with the serious nature of our brand."
    },
    {
        "id": "UCcw05gGzjLIs5dnxGkQHMvw",
        "title": "Sky Sports News",
        "thumbnail": "https://yt3.ggpht.com/ImUdu6TuUxSZVnPczkhVenR-hQXUhIwoPXUIvh8hrXBzyewK8Lt0q8N50PYqCihgHeimBLIC=s800-c-k-c0x00ffffff-no-rj",
        "subs": 1470000,
        "avg_views": 68926,
        "engagement_rate": 4.7,
        "video_count": 12480,
        "description": "The official YouTube channel for Sky Sports News. Your home of sports news on channel 409.",
        "match_reason": "This channel is a good match as it attracts a large, sports-oriented audience who values sustainability and ethical production, and its professional voice aligns well with our brand's serious commitment to these issues."
    },
    {
        "id": "UCja8sZ2T4ylIqjggA1Zuukg",
        "title": "CBS Sports",
        "thumbnail": "https://yt3.ggpht.com/jnGO8vkeg1R9IAaIHIej_SS9tzYXtyk54KwbHovEq2No3HfvV6mw2CYVIoFg2ThbFTnkUiSIBw=s800-c-k-c0x00ffffff-no-rj",
        "subs": 992000,
        "avg_views": 33649,
        "engagement_rate": 3.4,
        "video_count": 31278,
        "description": "Hello, friends",
        "match_reason": "CBS Sports is a good match for brand awareness as it has a large, diverse audience who value sustainability and ethical production, allowing for effective communication in a professional manner."
    },
    {
        "id": "UCi9ACGG8NptsQhaMyezITEw",
        "title": "Yahoo! Sports",
        "thumbnail": "https://yt3.ggpht.com/8gEXUsVuj6vUS0F2x2kCY0SvSTg0otwCPGwZl6ztN8vJOtcGfwIs48Oo-82CHbIyRzzzBQyFfw=s800-c-k-c0x00ffffff-no-rj",
        "subs": 320000,
        "avg_views": 26598,
        "engagement_rate": 8.3,
        "video_count": 9657,
        "description": "Your home for sports, all the time.",
        "match_reason": "Yahoo! Sports, a platform with a vast reach, aligns well with our brand's goal of awareness as it promotes sustainability and ethical production, thus providing an ideal space to connect with a professional and conscious audience."
    },
    {
        "id": "UCOGxnF5dWQtoEz6E-msabZA",
        "title": "CBC Sports",
        "thumbnail": "https://yt3.ggpht.com/cOLU9IIxcLh_2GL2vgETRarcvvWEx8NhL5eDThQwFIP09J3puTgvhfdmOl6vEizb38e9Z064EIs=s800-c-k-c0x00ffffff-no-rj",
        "subs": 272000,
        "avg_views": 21960,
        "engagement_rate": 8.1,
        "video_count": 11352,
        "description": "CBC Sports: The voice of Canadian athletes, fans and the Olympic Games",
        "match_reason": "CBC Sports is a great match as it is a highly respected platform that reaches a wide audience of Canadians who value sustainability and ethical production, and its professional tone aligns perfectly with our brand's goal of increasing awareness."
    }
]
  );
  
  const filteredInfluencers = computed(() => {
    if (!searchQuery.value) return influencers.value;
    
    const query = searchQuery.value.toLowerCase();
    return influencers.value.filter(influencer => 
      influencer.name.toLowerCase().includes(query) || 
      influencer.description.toLowerCase().includes(query) ||
      influencer.categories.some(category => category.toLowerCase().includes(query))
    );
  });
  
  const formatNumber = (num) => {
    if (num >= 1000000) {
      return (num / 1000000).toFixed(1) + 'M';
    } else if (num >= 1000) {
      return (num / 1000).toFixed(1) + 'K';
    }
    return num.toString();
  };

  const getInfluencers = async () => {
    const response = await fetch('http://localhost:8000/find-influencers', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(useColor().value)
    });
    influencers.value = await response.json();
  };

  getInfluencers();
  </script>
  
  