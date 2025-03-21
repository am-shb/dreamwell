<template>
  <li>
    <div class="px-4 py-4 sm:px-6">
      <div class="flex items-center justify-between">
        <div class="flex items-center">
          <div class="flex-shrink-0 h-10 w-10 rounded-full bg-purple-100 flex items-center justify-center">
            <component :is="campaign.icon" class="h-5 w-5 text-purple-600" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-purple-600">
              {{ campaign.name }}
            </p>
            <p class="text-sm text-gray-500">
              {{ campaign.influencers }} influencers • {{ campaign.platform }}
            </p>
          </div>
        </div>
        <div class="flex items-center">
          <span :class="[
            campaign.status === 'Active' ? 'bg-green-100 text-green-800' : 
            campaign.status === 'Pending' ? 'bg-yellow-100 text-yellow-800' : 
            'bg-gray-100 text-gray-800',
            'px-2 inline-flex text-xs leading-5 font-semibold rounded-full'
          ]">
            {{ campaign.status }}
          </span>
          <button class="ml-4 text-gray-400 hover:text-gray-500">
            <MoreVertical class="h-5 w-5" />
          </button>
        </div>
      </div>
      <div class="mt-2 sm:flex sm:justify-between">
        <div class="sm:flex">
          <p class="flex items-center text-sm text-gray-500">
            <Calendar class="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" />
            Started on {{ campaign.startDate }}
          </p>
          <p class="mt-2 flex items-center text-sm text-gray-500 sm:mt-0 sm:ml-6">
            <DollarSign class="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" />
            Budget: ${{ campaign.budget.toLocaleString() }}
          </p>
        </div>
        <div class="mt-2 flex items-center text-sm text-gray-500 sm:mt-0">
          <TrendingUp class="flex-shrink-0 mr-1.5 h-4 w-4 text-gray-400" />
          <p>
            {{ campaign.engagement.toLocaleString() }} engagements
          </p>
        </div>
      </div>
    </div>
  </li>
</template>

<script setup>
// import { Calendar, DollarSign, TrendingUp, MoreVertical } from 'lucide-vue-next';

defineProps({
  campaign: {
    type: Object,
    required: true
  }
});
</script>

