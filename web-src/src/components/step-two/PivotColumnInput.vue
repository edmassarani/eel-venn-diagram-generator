<script setup>
import SelectField from '@utils/SelectField.vue'
import { useSourceStore } from '@/stores/SourceStore'
import { computed } from 'vue'

const props = defineProps({
  index: {
    type: Number,
    required: true,
  },
})

const store = useSourceStore()

const name = computed(() => store.sources[props.index].name)
const columns = computed(() => store.sources[props.index].columns ?? [])

const pivotColumn = computed({
  get() {
    return store.sources[props.index].pivot ?? null
  },
  set: (value) => {
    store.setSourcePivotColumn(props.index, value)
  },
})
</script>

<template>
  <div class="relative rounded bg-white p-2">
    <h4 class="mb-2 text-xl font-bold">Source: {{ name }}</h4>

    <div class="pl-2">
      <SelectField
        v-model="pivotColumn"
        label="Pivot Column"
        class="mb-1"
        :tabindex="1"
        placeholder="Select a column from this data source"
        :options="columns"
        required
      />
    </div>
  </div>
</template>
