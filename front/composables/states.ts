export const useColor = () => useState('campaign', () => {return {
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
}})

export const useColor2 = () => useState('campaigns2', () => {return [
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
]})