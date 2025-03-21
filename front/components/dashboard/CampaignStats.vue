<template>
  <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 mb-6">
    <div class="bg-white overflow-hidden shadow rounded-lg">
      <div class="px-4 py-5 sm:p-6">
        <div class="flex items-center">
          <div class="flex-shrink-0 bg-purple-100 rounded-md p-3">
            <TrendingUp class="h-6 w-6 text-purple-600" />
          </div>
          <div class="ml-5 w-0 flex-1">
            <dl>
              <dt class="text-sm font-medium text-gray-500 truncate">
                Active Campaigns
              </dt>
              <dd>
                <div class="text-lg font-medium text-gray-900">{{ activeCampaigns }}</div>
              </dd>
            </dl>
          </div>
        </div>
      </div>
    </div>
    
    <div class="bg-white overflow-hidden shadow rounded-lg">
      <div class="px-4 py-5 sm:p-6">
        <div class="flex items-center">
          <div class="flex-shrink-0 bg-purple-100 rounded-md p-3">
            <Users class="h-6 w-6 text-purple-600" />
          </div>
          <div class="ml-5 w-0 flex-1">
            <dl>
              <dt class="text-sm font-medium text-gray-500 truncate">
                Total Influencers
              </dt>
              <dd>
                <div class="text-lg font-medium text-gray-900">{{ totalInfluencers }}</div>
              </dd>
            </dl>
          </div>
        </div>
      </div>
    </div>
    
    <div class="bg-white overflow-hidden shadow rounded-lg">
      <div class="px-4 py-5 sm:p-6">
        <div class="flex items-center">
          <div class="flex-shrink-0 bg-purple-100 rounded-md p-3">
            <BarChart class="h-6 w-6 text-purple-600" />
          </div>
          <div class="ml-5 w-0 flex-1">
            <dl>
              <dt class="text-sm font-medium text-gray-500 truncate">
                Total Engagement
              </dt>
              <dd>
                <div class="text-lg font-medium text-gray-900">{{ formatNumber(totalEngagement) }}</div>
              </dd>
            </dl>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
// import { TrendingUp, Users, BarChart } from 'lucide-vue-next';
import { useCampaignStore } from '../../store/campaign';

const { campaigns } = useCampaignStore();

const activeCampaigns = computed(() => 
  campaigns.value.filter(c => c.status === 'Active').length
);

const totalInfluencers = computed(() => 
  campaigns.value.reduce((sum, campaign) => sum + campaign.influencers, 0)
);

const totalEngagement = computed(() => 
  campaigns.value.reduce((sum, campaign) => sum + campaign.engagement, 0)
);

const formatNumber = (num) => {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M';
  } else if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'K';
  }
  return num.toString();
};
</script>

