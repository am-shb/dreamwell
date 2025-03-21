<template>
  <div class="space-y-6 transition-all duration-500">
    <div class="text-center mb-8">
      <h3 class="text-2xl font-bold text-gray-900">Campaign Summary</h3>
      <p class="mt-2 text-gray-600">Review your campaign details before launching</p>
    </div>
    
    <div class="max-w-3xl mx-auto">
      <div class="bg-purple-50 border border-purple-200 rounded-lg p-6 mb-6">
        <h4 class="text-xl font-bold text-purple-800 mb-4">{{ newCampaign.name }}</h4>
        <p class="text-gray-700 mb-4">{{ newCampaign.description }}</p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <div>
            <h5 class="font-medium text-purple-700 mb-2">Brand Personality</h5>
            <div class="flex flex-wrap gap-2">
              <span v-for="value in newCampaign.brandValues" :key="value" 
                class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800">
                {{ value }}
              </span>
            </div>
          </div>
          
          <div>
            <h5 class="font-medium text-purple-700 mb-2">Target Audience</h5>
            <p class="text-sm text-gray-600">Age: {{ newCampaign.ageRange }}</p>
            <p class="text-sm text-gray-600">Gender: {{ getGenderLabel(newCampaign.genderMix) }}</p>
            <p class="text-sm text-gray-600">Locations: {{ newCampaign.locations.join(', ') }}</p>
          </div>
          
          <div>
            <h5 class="font-medium text-purple-700 mb-2">Campaign Goal</h5>
            <p class="text-sm text-gray-600">{{ getCampaignGoalLabel(newCampaign.campaignGoal) }}</p>
            <p v-if="newCampaign.specificGoal" class="text-sm text-gray-600">
              Specific: {{ newCampaign.specificGoal }}
            </p>
          </div>
          
          <div>
            <h5 class="font-medium text-purple-700 mb-2">Content Style</h5>
            <p class="text-sm text-gray-600">{{ getBrandVoiceLabel(newCampaign.brandVoice) }}</p>
            <p v-if="newCampaign.customVoice" class="text-sm text-gray-600">
              {{ newCampaign.customVoice }}
            </p>
          </div>
          
          <div>
            <h5 class="font-medium text-red-700 mb-2">Content to Avoid</h5>
            <div class="flex flex-wrap gap-2">
              <span v-for="dealbreaker in newCampaign.dealbreakers" :key="dealbreaker" 
                class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">
                {{ dealbreaker }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCampaignStore } from '../../../store/campaign';

const { getGenderLabel, getCampaignGoalLabel, getBrandVoiceLabel } = useCampaignStore();
const newCampaign = useColor();
</script>

