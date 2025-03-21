<template>
  <div class="space-y-6 transition-all duration-500">
    <div class="text-center mb-8">
      <h3 class="text-2xl font-bold text-gray-900">Campaign North Star</h3>
      <p class="mt-2 text-gray-600">What's your #1 goal?</p>
    </div>
    
    <div class="max-w-3xl mx-auto">
      <div class="space-y-3">
        <button 
          v-for="(goal, index) in campaignGoals" 
          :key="index"
          @click="selectCampaignGoal(goal.value)"
          :class="[
            'w-full flex items-center px-6 py-4 border-2 rounded-xl text-left text-base font-medium transition-all duration-200',
            newCampaign.campaignGoal === goal.value
              ? 'border-purple-600 bg-purple-50 text-purple-700 shadow-md'
              : 'border-gray-300 bg-white text-gray-700 hover:bg-gray-50'
          ]"
        >
          <span class="text-2xl mr-3">{{ goal.emoji }}</span>
          <div>
            <div class="font-bold">{{ goal.label }}</div>
            <div class="text-sm text-gray-500">{{ goal.description }}</div>
          </div>
        </button>
        
        <!-- Custom goal input -->
        <div class="mt-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Specific Target:</label>
          <input 
            type="text" 
            v-model="newCampaign.specificGoal" 
            placeholder="Enter a specific goal or metric..." 
            class="shadow-sm focus:ring-purple-500 focus:border-purple-500 block w-full sm:text-sm border-gray-300 rounded-md"
            @focus="selectCampaignGoal('specific')"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCampaignStore } from '../../../store/campaign';

const { selectCampaignGoal } = useCampaignStore();
const newCampaign = useColor();

const campaignGoals = [
  { 
    value: 'awareness', 
    label: 'Brand Awareness', 
    emoji: '🚀',
    description: 'Reach new audiences and increase brand recognition'
  },
  { 
    value: 'sales', 
    label: 'Direct Sales', 
    emoji: '💰',
    description: 'Drive conversions with promo codes and product features'
  },
  { 
    value: 'engagement', 
    label: 'Engagement', 
    emoji: '🤳',
    description: 'Generate UGC, comments, shares, and community interaction'
  },
  { 
    value: 'authority', 
    label: 'Authority', 
    emoji: '🏆',
    description: 'Position your brand as an industry leader and expert'
  },
  { 
    value: 'specific', 
    label: 'Specific Target', 
    emoji: '🎯',
    description: 'Define your own custom campaign goal'
  },
];
</script>

