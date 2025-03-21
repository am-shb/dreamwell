<template>
  <div class="sm:hidden">
    <div class="pt-2 pb-3 space-y-1">
      <a 
        href="#" 
        @click.prevent="$emit('change-page', 'dashboard')"
        :class="[
          currentPage === 'dashboard' 
            ? 'bg-purple-50 border-purple-500 text-purple-700' 
            : 'border-transparent text-gray-600 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-800',
          'block pl-3 pr-4 py-2 border-l-4 text-base font-medium'
        ]"
      >
        Dashboard
      </a>
      <a 
        href="#" 
        @click.prevent="$emit('change-page', 'new-campaign')"
        :class="[
          currentPage === 'new-campaign' 
            ? 'bg-purple-50 border-purple-500 text-purple-700' 
            : 'border-transparent text-gray-600 hover:bg-gray-50 hover:border-gray-300 hover:text-gray-800',
          'block pl-3 pr-4 py-2 border-l-4 text-base font-medium'
        ]"
      >
        Launch Campaign
      </a>
    </div>
    <div class="pt-4 pb-3 border-t border-gray-200">
      <div class="flex items-center px-4">
        <div class="flex-shrink-0">
          <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
        </div>
        <div class="ml-3">
          <div class="text-base font-medium text-gray-800">Tom Cook</div>
          <div class="text-sm font-medium text-gray-500">tom@example.com</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  currentPage: {
    type: String,
    required: true
  }
});

defineEmits(['change-page']);
</script>

