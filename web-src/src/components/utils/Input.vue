<script setup>
const props = defineProps({
  hasLabel: {
    type: Boolean,
    default: true,
  },

  label: String,

  labelClass: String,

  type: {
    type: String,
    default: 'text',
  },

  required: Boolean,
});
</script>

<template>
  <div>
    <label v-if="hasLabel" :class="labelClass">
      <span class="block">
        {{ label }}
      </span>

      <input
        :type="type"
        class="border border-gray-600 rounded w-full p-1"
        v-bind="$attrs"
      />
    </label>
  </div>
</template>
