<template>
  <div class="flex justify-between mt-8">
    <button 
      v-if="currentStep > 0" 
      @click="$emit('back')" 
      class="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none"
    >
      Back
    </button>
    <div v-else></div>
    
    <button 
      v-if="currentStep < totalSteps - 1" 
      @click="$emit('next')" 
      class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-purple-600 hover:bg-purple-700 focus:outline-none"
      :disabled="!canProceed"
    >
      Continue
    </button>
    
    <button 
      v-else 
      @click="$emit('finish')" 
      class="inline-flex items-center px-6 py-3 border border-transparent shadow-sm text-base font-medium rounded-md text-white bg-purple-600 hover:bg-purple-700 focus:outline-none"
    >
      Launch Campaign
    </button>
  </div>
</template>

<script setup>
defineProps({
  currentStep: {
    type: Number,
    required: true
  },
  totalSteps: {
    type: Number,
    required: true
  },
  canProceed: {
    type: Boolean,
    default: true
  }
});

defineEmits(['back', 'next', 'finish']);
</script>

