<template>
  <div class="space-y-6 transition-all duration-500">
    <div class="text-center mb-8">
      <h3 class="text-2xl font-bold text-gray-900">Let's start with the basics</h3>
      <p class="mt-2 text-gray-600">Give your campaign a name and describe what you're looking to achieve</p>
    </div>
    
    <div class="max-w-2xl mx-auto">
      <div class="mb-6">
        <label for="campaign-name" class="block text-sm font-medium text-gray-700 mb-1">Campaign name</label>
        <input type="text" id="campaign-name" v-model="newCampaign.name" 
          class="shadow-sm focus:ring-purple-500 focus:border-purple-500 block w-full text-lg border-gray-300 rounded-md py-3 px-4" 
          placeholder="Summer Collection Launch" />
      </div>

      <div>
        <label for="description" class="block text-sm font-medium text-gray-700 mb-1">Campaign description</label>
        <textarea id="description" v-model="newCampaign.description" rows="4" 
          class="shadow-sm focus:ring-purple-500 focus:border-purple-500 block w-full text-lg border-gray-300 rounded-md py-3 px-4"
          placeholder="Describe your campaign goals and what you want to achieve..."></textarea>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCampaignStore } from '../../../store/campaign';

const newCampaign = useColor();
// const camp = useColor();
// camp.value.name = 'test';
// console.log(camp.value);
</script>

