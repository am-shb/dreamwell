<template>
  <div class="space-y-6 transition-all duration-500">
    <div class="text-center mb-8">
      <h3 class="text-2xl font-bold text-gray-900">Content Vibe Check</h3>
      <p class="mt-2 text-gray-600">Choose the brand voice that fits best:</p>
    </div>
    
    <div class="max-w-3xl mx-auto">
      <div class="grid grid-cols-1 gap-4">
        <button 
          v-for="(voice, index) in brandVoices" 
          :key="index"
          @click="selectBrandVoice(voice.value)"
          :class="[
            'flex items-start px-6 py-4 border-2 rounded-xl text-left transition-all duration-200',
            newCampaign.brandVoice === voice.value
              ? 'border-purple-600 bg-purple-50 text-purple-700 shadow-md'
              : 'border-gray-300 bg-white text-gray-700 hover:bg-gray-50'
          ]"
        >
          <span class="text-2xl mr-3 mt-1">{{ voice.emoji }}</span>
          <div>
            <div class="font-bold text-base">{{ voice.label }}</div>
            <div class="text-sm text-gray-500">{{ voice.description }}</div>
          </div>
        </button>
        
        <!-- Custom voice input -->
        <div class="mt-2">
          <label class="block text-sm font-medium text-gray-700 mb-1">Other:</label>
          <div class="flex">
            <input 
              type="text" 
              v-model="customBrandVoice" 
              placeholder="Describe your brand voice..." 
              class="flex-grow shadow-sm focus:ring-purple-500 focus:border-purple-500 block w-full sm:text-sm border-gray-300 rounded-l-md"
              @focus="newCampaign.brandVoice = 'custom'"
            />
            <button 
              @click="addCustomBrandVoice"
              :disabled="!customBrandVoice"
              class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-r-md text-white bg-purple-600 hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Set
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

const { selectBrandVoice } = useCampaignStore();
const newCampaign = useColor();

const customBrandVoice = ref('');

const brandVoices = [
  { 
    value: 'playful', 
    label: 'Playful & Trendy', 
    emoji: '🎉',
    description: 'Gen Z slang, memes, and current cultural references'
  },
  { 
    value: 'expert', 
    label: 'Expert & Analytical', 
    emoji: '🧠',
    description: 'Data-driven, educational, whitepaper style content'
  },
  { 
    value: 'authentic', 
    label: 'Authentic & Raw', 
    emoji: '❤️',
    description: 'Unedited, "real talk" that feels genuine and unfiltered'
  },
  { 
    value: 'polished', 
    label: 'Polished & Aspirational', 
    emoji: '✨',
    description: 'High production value content that showcases an ideal lifestyle'
  },
];

const addCustomBrandVoice = () => {
  if (customBrandVoice.value) {
    newCampaign.value.brandVoice = 'custom';
    newCampaign.value.customVoice = customBrandVoice.value;
  }
};
</script>

