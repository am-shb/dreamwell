<template>
  <nav class="bg-white shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <div class="flex-shrink-0 flex items-center">
            <h1 class="text-xl font-bold text-purple-600">InfluencerHub</h1>
          </div>
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            <a 
              href="#" 
              @click.prevent="$emit('change-page', 'dashboard')"
              :class="[
                currentPage === 'dashboard' 
                  ? 'border-purple-500 text-gray-900' 
                  : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700',
                'inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium'
              ]"
            >
              Dashboard
            </a>
            <a 
              href="#" 
              @click.prevent="$emit('change-page', 'new-campaign')"
              :class="[
                currentPage === 'new-campaign' 
                  ? 'border-purple-500 text-gray-900' 
                  : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700',
                'inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium'
              ]"
            >
              Launch Campaign
            </a>
          </div>
        </div>
        <div class="hidden sm:ml-6 sm:flex sm:items-center">
          <div class="ml-3 relative">
            <div class="flex items-center">
              <button class="bg-white p-1 rounded-full text-gray-400 hover:text-gray-500 focus:outline-none">
                <Bell class="h-6 w-6" />
              </button>
              <div class="ml-3 flex items-center">
                <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                <span class="ml-2 text-sm font-medium text-gray-700">Tom Cook</span>
              </div>
            </div>
          </div>
        </div>
        <div class="-mr-2 flex items-center sm:hidden">
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen" 
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none"
          >
            <Menu v-if="!mobileMenuOpen" class="block h-6 w-6" />
            <X v-else class="block h-6 w-6" />
          </button>
        </div>
      </div>
    </div>

    <MobileMenu 
      v-if="mobileMenuOpen" 
      :currentPage="currentPage" 
      @change-page="(page) => { $emit('change-page', page); mobileMenuOpen = false; }" 
    />
  </nav>
</template>

<script setup>
import { ref } from 'vue';
// import { Bell, Menu, X } from 'lucide-vue-next';
import MobileMenu from './MobileMenu.vue';

defineProps({
  currentPage: {
    type: String,
    required: true
  }
});

defineEmits(['change-page']);

const mobileMenuOpen = ref(false);
</script>

