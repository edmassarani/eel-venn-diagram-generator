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

const { isAtMinCapacity } = storeToRefs(store)

const name = computed({
  get() {
    return store.sources[props.index].name
  },
  set: debounce((value) => {
    store.setSourceName(props.index, value)
  }, 200),
})

const file = computed(() => store.sources[props.index].file)

const getFilePath = async () => {
  // eslint-disable-next-line no-undef
  const path = await eel.get_file_path()()

  store.setSourceFile(props.index, path)
}

const removeSource = () => {
  store.removeSource(props.index)
}
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
      <div class="flex items-center">
        <div class="relative mr-2 mt-2">
          <input
            type="button"
            class="cursor-pointer rounded border border-gray-500 p-1"
            value="Select file"
            :tabindex="1"
            required
            @click="getFilePath"
          />
          <input
            type="text"
            name="file"
            :value="file"
            required
            class="absolute inset-x-1/2 bottom-0 h-px w-px opacity-0"
            tabindex="-1"
            @keypress.prevent="false"
          />
        </div>
        <p>{{ file }}</p>
      </div>
    </div>

    <button
      v-if="!isAtMinCapacity"
      type="button"
      class="absolute right-2 top-2"
      title="Remove data source"
      tabindex="2"
      @click="removeSource"
    >
      <svg-icon type="mdi" :path="mdiClose"></svg-icon>
    </button>
  </div>
</template>
