<template>
  <div class="min-h-screen bg-gray-50">
    <NuxtRouteAnnouncer />

    <AppHeader 
      :currentPage="currentPage" 
      @change-page="currentPage = $event"
    />
    
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import AppHeader from './components/layout/AppHeader.vue';
import Dashboard from './components/dashboard/Dashboard.vue';
import CampaignWizard from './components/campaign-wizard/CampaignWizard.vue';

// State management
const currentPage = ref('dashboard');
</script>

