<template>
  <div class="space-y-6 transition-all duration-500">
    <div class="text-center mb-8">
      <h3 class="text-2xl font-bold text-gray-900">Brand Personality DNA</h3>
      <p class="mt-2 text-gray-600">Which 3 words define your brand's core values?</p>
    </div>
    
    <div class="max-w-3xl mx-auto">
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
        <button 
          v-for="(value, index) in brandValues" 
          :key="index"
          @click="toggleBrandValue(value.name)"
          :disabled="!newCampaign.brandValues.includes(value.name) && newCampaign.brandValues.length >= 3"
          :class="[
            'flex items-center justify-center px-4 py-3 border-2 rounded-xl text-base font-medium transition-all duration-200',
            newCampaign.brandValues.includes(value.name)
              ? 'border-purple-600 bg-purple-50 text-purple-700 shadow-md transform scale-105'
              : 'border-gray-300 bg-white text-gray-700 hover:bg-gray-50',
            newCampaign.brandValues.length >= 3 && !newCampaign.brandValues.includes(value.name)
              ? 'opacity-50 cursor-not-allowed'
              : ''
          ]"
        >
          <span class="mr-2 text-xl">{{ value.emoji }}</span>
          {{ value.name }}
        </button>
        
        <!-- Custom value input -->
        <div class="col-span-2 sm:col-span-4 mt-3">
          <div class="flex">
            <input 
              type="text" 
              v-model="customBrandValue" 
              placeholder="Other value..." 
              class="flex-grow shadow-sm focus:ring-purple-500 focus:border-purple-500 block w-full sm:text-sm border-gray-300 rounded-l-md"
              :disabled="newCampaign.brandValues.length >= 3 && !newCampaign.brandValues.includes(customBrandValue) && customBrandValue !== ''"
            />
            <button 
              @click="addCustomBrandValue"
              :disabled="!customBrandValue || (newCampaign.brandValues.length >= 3 && !newCampaign.brandValues.includes(customBrandValue))"
              class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-r-md text-white bg-purple-600 hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Add
            </button>
          </div>
        </div>
      </div>
      
      <div class="mt-4 text-sm text-gray-500 flex items-center">
        <span class="mr-2">Selected:</span>
        <div class="flex flex-wrap gap-2">
          <span 
            v-for="(value, index) in newCampaign.brandValues" 
            :key="index"
            class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-purple-100 text-purple-800"
          >
            {{ value }}
            <button @click="toggleBrandValue(value)" class="ml-1.5 text-purple-600 hover:text-purple-800">
              <X class="h-3 w-3" />
            </button>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
// import { X } from 'lucide-vue-next';
import { useCampaignStore } from '../../../store/campaign';

const { toggleBrandValue } = useCampaignStore();
const newCampaign = useColor();

const customBrandValue = ref('');

const brandValues = [
  { name: 'Sustainability', emoji: '🌱' },
  { name: 'Innovation', emoji: '💡' },
  { name: 'Luxury', emoji: '✨' },
  { name: 'Adventure', emoji: '🏔️' },
  { name: 'Community', emoji: '🤝' },
  { name: 'Humor', emoji: '😂' },
  { name: 'Empowerment', emoji: '✊' },
];

const addCustomBrandValue = () => {
  if (customBrandValue.value && newCampaign.value.brandValues.length < 3) {
    newCampaign.value.brandValues.push(customBrandValue.value);
    customBrandValue.value = '';
  }
};
</script>

