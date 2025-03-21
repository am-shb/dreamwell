<template>
  <div>
    <!-- Progress bar -->
    <div class="w-full bg-gray-200 rounded-full h-2.5 mb-6">
      <div class="bg-purple-600 h-2.5 rounded-full transition-all duration-500" 
           :style="{ width: `${(currentStep / totalSteps) * 100}%` }"></div>
    </div>

    <!-- Step indicators -->
    <div class="flex justify-between mb-8 relative">
      <div class="absolute top-4 left-0 right-0 h-0.5 bg-gray-300 -z-10"></div>
      <div v-for="step in totalSteps" :key="step" 
        :class="[
          'relative flex items-center justify-center w-8 h-8 rounded-full border-2 transition-all duration-300 z-10 bg-white',
          currentStep >= step 
            ? 'border-purple-600 bg-purple-600 text-white' 
            : 'border-gray-300 bg-white text-gray-400'
        ]">
        <span class="text-sm font-medium">{{ step }}</span>
      </div>
    </div>
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
  }
});
</script>

