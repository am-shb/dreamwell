<template>
  <div>
    <div class="md:flex md:items-center md:justify-between mb-6">
      <div class="flex-1 min-w-0">
        <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl sm:truncate">
          Campaign Dashboard
        </h2>
      </div>
      <div class="mt-4 flex md:mt-0 md:ml-4">
        <button 
          @click="$emit('new-campaign')" 
          class="ml-3 inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-purple-600 hover:bg-purple-700 focus:outline-none"
        >
          <PlusCircle class="h-4 w-4 mr-2" />
          New Campaign
        </button>
      </div>
    </div>

    <CampaignStats />
    <CampaignList :campaigns="campaigns" />
  </div>
</template>

<script setup>
// import { PlusCircle } from 'lucide-vue-next';
import CampaignStats from './CampaignStats.vue';
import CampaignList from './CampaignList.vue';
import { useCampaignStore } from '../../store/campaign';

const campaigns = useColor2();

defineEmits(['new-campaign']);
</script>

