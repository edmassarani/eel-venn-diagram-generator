<script setup>
import PageTitle from '@utils/PageTitle.vue'
import { useSourceStore } from '@/stores/SourceStore'
import PivotColumnInput from './PivotColumnInput.vue'
import { storeToRefs } from 'pinia'

const store = useSourceStore()

const { sourceCount } = storeToRefs(store)
</script>

<template>
  <div class="flex min-h-0 flex-col p-4">
    <page-title>Step 2: Select Pivot Column</page-title>

    <p class="mb-2">
      Select the column that is common in each source to evaluate the
      intersections
    </p>

    <div class="mb-4 overflow-auto bg-gray-200 p-4">
      <PivotColumnInput
        v-for="i in sourceCount"
        :key="i"
        :index="i - 1"
        class="mb-4 last:mb-0"
      />
    </div>
  </div>
</template>
