<script setup>
import PageTitle from '../utils/PageTitle.vue'
import DataSourceInput from './DataSourceInput.vue'

defineProps({
  sourceCount: {
    type: Number,
    required: true,
  },
})
</script>

<template>
  <div class="p-4">
    <page-title>Step 1: Add Data Sources</page-title>

    <p class="mb-2">
      Add your data source files here, only CSV files are allowed
    </p>

    <form @submit.prevent>
      <DataSourceInput v-for="i in sourceCount" :index="i" :key="i" />
    </form>
    <!-- create button to add new source (min 2, max 6) -->
    <!-- create component to navigate through steps -->
  </div>
</template>
