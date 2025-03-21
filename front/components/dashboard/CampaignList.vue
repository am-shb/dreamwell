<template>
  <div class="bg-white shadow overflow-hidden sm:rounded-md">
    <ul class="divide-y divide-gray-200">
      <CampaignItem 
        v-for="(campaign, index) in campaigns" 
        :key="index" 
        :campaign="campaign" 
      />
    </ul>
  </div>
</template>

<script setup>
import CampaignItem from './CampaignItem.vue';

defineProps({
  campaigns: {
    type: Array,
    required: true
  }
});
</script>

