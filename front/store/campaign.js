import { ref } from "vue"
// import { Instagram, Youtube, Twitter, MessageSquare } from "lucide-vue-next"

// Create a composable store
export function useCampaignStore() {
  // Sample campaign data
  const campaigns = ref([
    {
      name: "Summer Collection Launch",
      influencers: 24,
      platform: "Instagram",
      status: "Active",
      startDate: "May 15, 2023",
      budget: 50000,
      engagement: 345000,
      // icon: Instagram,
    },
    {
      name: "Product Review Series",
      influencers: 12,
      platform: "YouTube",
      status: "Active",
      startDate: "April 3, 2023",
      budget: 75000,
      engagement: 520000,
      // icon: Youtube,
    },
    {
      name: "Brand Awareness Campaign",
      influencers: 35,
      platform: "Twitter",
      status: "Pending",
      startDate: "June 1, 2023",
      budget: 30000,
      engagement: 0,
      // icon: Twitter,
    },
    {
      name: "Customer Testimonials",
      influencers: 8,
      platform: "Multiple",
      status: "Completed",
      startDate: "January 10, 2023",
      budget: 25000,
      engagement: 280000,
      // icon: MessageSquare,
    },
  ])

  // New campaign form data
  const newCampaign = useColor();

  // Helper data
  const genderOptions = [
    { value: "female", label: "Mostly Female", emoji: "♀️" },
    { value: "male", label: "Mostly Male", emoji: "♂️" },
    { value: "balanced", label: "Balanced", emoji: "⚖️" },
  ]

  const campaignGoals = [
    {
      value: "awareness",
      label: "Brand Awareness",
      emoji: "🚀",
      description: "Reach new audiences and increase brand recognition",
    },
    {
      value: "sales",
      label: "Direct Sales",
      emoji: "💰",
      description: "Drive conversions with promo codes and product features",
    },
    {
      value: "engagement",
      label: "Engagement",
      emoji: "🤳",
      description: "Generate UGC, comments, shares, and community interaction",
    },
    {
      value: "authority",
      label: "Authority",
      emoji: "🏆",
      description: "Position your brand as an industry leader and expert",
    },
    {
      value: "specific",
      label: "Specific Target",
      emoji: "🎯",
      description: "Define your own custom campaign goal",
    },
  ]

  const brandVoices = [
    {
      value: "playful",
      label: "Playful & Trendy",
      emoji: "🎉",
      description: "Gen Z slang, memes, and current cultural references",
    },
    {
      value: "expert",
      label: "Expert & Analytical",
      emoji: "🧠",
      description: "Data-driven, educational, whitepaper style content",
    },
    {
      value: "authentic",
      label: "Authentic & Raw",
      emoji: "❤️",
      description: 'Unedited, "real talk" that feels genuine and unfiltered',
    },
    {
      value: "polished",
      label: "Polished & Aspirational",
      emoji: "✨",
      description: "High production value content that showcases an ideal lifestyle",
    },
  ]

  // Methods
  const toggleBrandValue = (value) => {
    const index = newCampaign.value.brandValues.indexOf(value)
    if (index === -1) {
      if (newCampaign.value.brandValues.length < 3) {
        newCampaign.value.brandValues.push(value)
      }
    } else {
      newCampaign.value.brandValues.splice(index, 1)
    }
  }

  const toggleLocation = (location) => {
    const index = newCampaign.value.locations.indexOf(location)
    if (index === -1) {
      newCampaign.value.locations.push(location)
    } else {
      newCampaign.value.locations.splice(index, 1)
    }
  }

  const selectCampaignGoal = (goal) => {
    newCampaign.value.campaignGoal = goal
  }

  const selectBrandVoice = (voice) => {
    newCampaign.value.brandVoice = voice
  }

  const toggleDealbreaker = (dealbreaker) => {
    const index = newCampaign.value.dealbreakers.indexOf(dealbreaker)
    if (index === -1) {
      newCampaign.value.dealbreakers.push(dealbreaker)
    } else {
      newCampaign.value.dealbreakers.splice(index, 1)
    }
  }

  const getGenderLabel = (value) => {
    const option = genderOptions.find((opt) => opt.value === value)
    return option ? option.label : value
  }

  const getCampaignGoalLabel = (value) => {
    const goal = campaignGoals.find((g) => g.value === value)
    return goal ? goal.label : value
  }

  const getBrandVoiceLabel = (value) => {
    const voice = brandVoices.find((v) => v.value === value)
    return voice ? voice.label : value
  }

  const formatDate = (dateString) => {
    if (!dateString) return ""
    const date = new Date(dateString)
    return date.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" })
  }

  const addCampaign = () => {
    // Add the campaign to the list
    campaigns.value.unshift({
      name: newCampaign.value.name,
      influencers: 10, // Default value
      platform: "Multiple",
      status: "Pending",
      startDate: new Date().toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" }),
      budget: 25000, // Default value
      engagement: 0,
      // icon: MessageSquare,
    })
  }

  const resetCampaignForm = () => {
    newCampaign.value = {
      name: "",
      description: "",
      budget: null,
      startDate: "",
      endDate: "",
      ageRange: "18-24",
      genderMix: "balanced",
      locations: ["Global"],
      platform: "Instagram",
      brandValues: [],
      campaignGoal: "",
      specificGoal: "",
      brandVoice: "",
      customVoice: "",
      dealbreakers: [],
      influencerCount: 10,
    }
  }

  return {
    campaigns,
    newCampaign,
    toggleBrandValue,
    toggleLocation,
    selectCampaignGoal,
    selectBrandVoice,
    toggleDealbreaker,
    getGenderLabel,
    getCampaignGoalLabel,
    getBrandVoiceLabel,
    formatDate,
    addCampaign,
    resetCampaignForm,
  }
}

