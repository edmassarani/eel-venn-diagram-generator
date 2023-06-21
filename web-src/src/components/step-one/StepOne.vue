<script setup>
import { mdiPlus } from '@mdi/js'
import SvgIcon from '@jamescoyle/vue-icon'
import PageTitle from '@utils/PageTitle.vue'
import DataSourceInput from './DataSourceInput.vue'
import { useSourceStore } from '@/stores/SourceStore'
import TextButton from '@utils/TextButton.vue'
import { storeToRefs } from 'pinia'

const store = useSourceStore()

const { isAtMaxCapacity, sourceCount } = storeToRefs(store)

const addSource = (e) => {
  store.addSource()
}
</script>

<template>
  <div class="flex min-h-0 flex-col p-4">
    <page-title>Step 1: Add Data Sources</page-title>

    <p class="mb-2">
      Add your data source files here, only CSV files are allowed
    </p>

    <div class="mb-4 overflow-auto bg-gray-200 p-4">
      <DataSourceInput
        v-for="i in sourceCount"
        :key="i"
        :index="i - 1"
        class="mb-4 last:mb-0"
      />
    </div>

    <text-button
      v-if="!isAtMaxCapacity"
      class="mb-2 flex items-center justify-center"
      @click="addSource"
    >
      <svg-icon type="mdi" :path="mdiPlus"></svg-icon>
      <span>Add Source</span>
    </text-button>
  </div>
</template>
