<template>
  <div class="space-y-8 transition-all duration-500">
    <div class="text-center mb-8">
      <h3 class="text-2xl font-bold text-gray-900">Bullseye Audience</h3>
      <p class="mt-2 text-gray-600">Tell us about your ideal customer</p>
    </div>
    
    <div class="max-w-3xl mx-auto">
      <!-- Age Range -->
      <div class="mb-8">
        <h4 class="text-lg font-medium text-gray-900 mb-3">A) Age:</h4>
        <div class="grid grid-cols-2 sm:grid-cols-5 gap-3">
          <button 
            v-for="age in ageRanges" 
            :key="age"
            @click="newCampaign.ageRange = age"
            :class="[
              'px-4 py-3 border-2 rounded-lg text-base font-medium transition-all duration-200',
              newCampaign.ageRange === age
                ? 'border-purple-600 bg-purple-50 text-purple-700 shadow-md'
                : 'border-gray-300 bg-white text-gray-700 hover:bg-gray-50'
            ]"
          >
            {{ age }}
          </button>
        </div>
      </div>
      
      <!-- Gender Mix -->
      <div class="mb-8">
        <h4 class="text-lg font-medium text-gray-900 mb-3">B) Gender Mix:</h4>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <button 
            v-for="(gender, index) in genderOptions" 
            :key="index"
            @click="newCampaign.genderMix = gender.value"
            :class="[
              'flex items-center justify-center px-4 py-3 border-2 rounded-lg text-base font-medium transition-all duration-200',
              newCampaign.genderMix === gender.value
                ? 'border-purple-600 bg-purple-50 text-purple-700 shadow-md'
                : 'border-gray-300 bg-white text-gray-700 hover:bg-gray-50'
            ]"
          >
            <span class="mr-2 text-xl">{{ gender.emoji }}</span>
            {{ gender.label }}
          </button>
        </div>
      </div>
      
      <!-- Top Locations -->
      <div>
        <h4 class="text-lg font-medium text-gray-900 mb-3">C) Top Locations:</h4>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <button 
            v-for="location in locations" 
            :key="location"
            @click="toggleLocation(location)"
            :class="[
              'px-4 py-3 border-2 rounded-lg text-base font-medium transition-all duration-200',
              newCampaign.locations.includes(location)
                ? 'border-purple-600 bg-purple-50 text-purple-700 shadow-md'
                : 'border-gray-300 bg-white text-gray-700 hover:bg-gray-50'
            ]"
          >
            {{ location }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCampaignStore } from '../../../store/campaign';

const { toggleLocation } = useCampaignStore();
const newCampaign = useColor();

const ageRanges = ['13-17', '18-24', '25-34', '35-44', '45+'];

const genderOptions = [
  { value: 'female', label: 'Mostly Female', emoji: '♀️' },
  { value: 'male', label: 'Mostly Male', emoji: '♂️' },
  { value: 'balanced', label: 'Balanced', emoji: '⚖️' },
];

const locations = ['North America', 'Europe', 'SE Asia', 'Global'];
</script>

