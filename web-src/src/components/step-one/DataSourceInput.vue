<script setup>
import { mdiClose } from '@mdi/js'
import SvgIcon from '@jamescoyle/vue-icon'
import InputField from '../utils/InputField.vue'
import { useSourceStore } from '@/stores/SourceStore'
import { computed } from 'vue'
import { debounce } from 'lodash'
import { storeToRefs } from 'pinia'

const props = defineProps({
  index: {
    type: Number,
    required: true,
  },
})

const store = useSourceStore()

const name = computed({
  get() {
    return store.sources[props.index].name
  },
  set: debounce((value) => {
    store.setSourceName(props.index, value)
  }, 200),
})

const file = computed({
  get() {
    return store.sources[props.index].name
  },
  set(value) {
    store.setSourceFile(props.index, value)
  },
})

const removeSource = () => {
  store.removeSource(props.index)
}

const { isAtMinCapacity } = storeToRefs(store)
</script>

<template>
  <div class="relative rounded bg-white p-2">
    <h4 class="mb-2 text-xl font-bold">Data Source {{ index + 1 }}</h4>

    <div class="pl-2">
      <InputField
        v-model="name"
        label="Source Name"
        class="mb-1"
        placeholder="Enter a name for this source"
        :tabindex="1"
        required
      />
      <InputField
        label="Source File"
        type="file"
        class="border-0 pl-0"
        accept="text/csv"
        :tabindex="1"
        required
        @update:model-value="file = $event"
      />
    </div>

    <button
      type="button"
      class="absolute right-2 top-2"
      title="Remove data source"
      tabindex="2"
      @click="removeSource"
    >
      <svg-icon v-if="!isAtMinCapacity" type="mdi" :path="mdiClose"></svg-icon>
    </button>
  </div>
</template>
