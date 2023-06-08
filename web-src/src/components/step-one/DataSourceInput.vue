<script setup>
import InputField from '../utils/InputField.vue'

defineProps({
  index: {
    type: Number,
    required: true,
  },
})
</script>

<template>
  <div class="mb-4 rounded bg-gray-200 p-4">
    <h4 class="mb-2 text-xl font-bold">Data Source {{ index }}</h4>

    <div class="pl-2">
      <InputField
        label="Source Name"
        class="mb-1"
        placeholder="Enter a name for this source"
        required
      />
      <InputField
        label="Source File"
        type="file"
        class="border-0"
        accept="text/csv"
        required
      />
    </div>
  </div>
</template>
