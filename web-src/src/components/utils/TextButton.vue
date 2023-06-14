<script setup>
defineProps({
  type: {
    type: String,
    default: 'button',
  },

  disabled: {
    type: Boolean,
    default: false,
  },
})
</script>

<template>
  <button
    :type="type"
    class="w-full rounded border border-gray-600 p-1 hover:bg-gray-200"
    :class="[disabled ? 'cursor-not-allowed' : '']"
    v-bind="$attrs"
  >
    <slot></slot>
  </button>
</template>
