<template>
  <div class="space-y-6 transition-all duration-500">
    <div class="text-center mb-8">
      <h3 class="text-2xl font-bold text-gray-900">Dealbreaker Alert</h3>
      <p class="mt-2 text-gray-600">What content style can't you associate with?</p>
    </div>
    
    <div class="max-w-3xl mx-auto">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button 
          v-for="(dealbreaker, index) in dealbreakers" 
          :key="index"
          @click="toggleDealbreaker(dealbreaker.value)"
          :class="[
            'flex items-center px-4 py-3 border-2 rounded-xl text-base font-medium transition-all duration-200',
            newCampaign.dealbreakers.includes(dealbreaker.value)
              ? 'border-red-500 bg-red-50 text-red-700 shadow-md'
              : 'border-gray-300 bg-white text-gray-700 hover:bg-gray-50'
          ]"
        >
          <span class="mr-2 text-xl">{{ dealbreaker.emoji }}</span>
          {{ dealbreaker.label }}
        </button>
        
        <!-- Custom dealbreaker input -->
        <div class="col-span-1 sm:col-span-2 mt-3">
          <div class="flex">
            <input 
              type="text" 
              v-model="customDealbreaker" 
              placeholder="Other dealbreaker..." 
              class="flex-grow shadow-sm focus:ring-purple-500 focus:border-purple-500 block w-full sm:text-sm border-gray-300 rounded-l-md"
            />
            <button 
              @click="addCustomDealbreaker"
              :disabled="!customDealbreaker"
              class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-r-md text-white bg-purple-600 hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Add
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCampaignStore } from '../../../store/campaign';

const { toggleDealbreaker } = useCampaignStore();
const newCampaign = useColor();

const customDealbreaker = ref('');

const dealbreakers = [
  { value: 'Political commentary', emoji: '🗳️', label: 'Political commentary' },
  { value: 'Controversial humor', emoji: '😈', label: 'Controversial humor' },
  { value: 'Heavy sponsorships', emoji: '💼', label: 'Heavy sponsorships' },
  { value: 'Minimalist aesthetics', emoji: '⚪', label: 'Minimalist aesthetics' },
  { value: 'Vibrant/chaotic edits', emoji: '🌈', label: 'Vibrant/chaotic edits' },
];

const addCustomDealbreaker = () => {
  if (customDealbreaker.value) {
    newCampaign.value.dealbreakers.push(customDealbreaker.value);
    customDealbreaker.value = '';
  }
};
</script>

