<template>
  <div>
    <div class="md:flex md:items-center md:justify-between mb-6">
      <div class="flex-1 min-w-0">
        <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl sm:truncate">
          Launch New Campaign
        </h2>
      </div>
    </div>

    <WizardProgress :currentStep="currentStep" :totalSteps="totalSteps" />

    <div class="bg-white shadow overflow-hidden sm:rounded-lg p-6">
      <!-- Step components -->
      <BasicInfo v-if="currentStep === 0" />
      <BrandPersonality v-if="currentStep === 1" />
      <TargetAudience v-if="currentStep === 2" />
      <CampaignGoal v-if="currentStep === 3" />
      <ContentStyle v-if="currentStep === 4" />
      <Dealbreakers v-if="currentStep === 5" />
      <Summary v-if="currentStep === 6" />

      <WizardNavigation 
        :currentStep="currentStep" 
        :totalSteps="totalSteps" 
        :canProceed="canProceed"
        @back="currentStep--"
        @next="nextStep"
        @finish="launchCampaign"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import WizardProgress from './WizardProgress.vue';
import WizardNavigation from './WizardNavigation.vue';
import BasicInfo from './steps/BasicInfo.vue';
import BrandPersonality from './steps/BrandPersonality.vue';
import TargetAudience from './steps/TargetAudience.vue';
import CampaignGoal from './steps/CampaignGoal.vue';
import ContentStyle from './steps/ContentStyle.vue';
import Dealbreakers from './steps/Dealbreakers.vue';
import Summary from './steps/Summary.vue';
import { useCampaignStore } from '../../store/campaign';

const currentStep = ref(0);
const totalSteps = 7; // 0-indexed, so this is 7 steps total
const { addCampaign, resetCampaignForm } = useCampaignStore();
const newCampaign = useColor();

const nextStep = () => {
  if (currentStep.value < totalSteps - 1) {
    currentStep.value++;
  }
};

const launchCampaign = () => {
  addCampaign();
  // resetCampaignForm();
  currentStep.value = 0;
  navigateTo('/sub');
};

const canProceed = computed(() => {
  switch (currentStep.value) {
    case 0:
      return newCampaign.value.name && newCampaign.value.description;
    case 1:
      return newCampaign.value.brandValues.length > 0;
    case 2:
      return newCampaign.value.ageRange && newCampaign.value.genderMix && newCampaign.value.locations.length > 0;
    case 3:
      return newCampaign.value.campaignGoal || newCampaign.value.specificGoal;
    case 4:
      return newCampaign.value.brandVoice;
    case 5:
      return true; // Dealbreakers are optional
    default:
      return true;
  }
});

const emit = defineEmits(['finish']);
</script>

