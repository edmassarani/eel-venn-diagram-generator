<script setup>
import Input from '../utils/Input.vue';

const props = defineProps({
  index: {
    type: Number,
    required: true,
  },
});
</script>

<template>
  <div class="bg-gray-200 p-4 mb-4 rounded">
    <h4 class="text-xl font-bold mb-2">Data Source {{ index }}</h4>

    <div class="pl-2">
      <Input
        label="Source Name"
        class="mb-1"
        placeholder="Enter a name for this source"
        required
      />
      <Input
        label="Source File"
        type="file"
        class="border-0"
        accept="text/csv"
        required
      />
    </div>
  </div>
</template>
