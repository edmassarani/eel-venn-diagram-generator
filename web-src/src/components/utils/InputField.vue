<script setup>
defineProps({
  hasLabel: {
    type: Boolean,
    default: true,
  },

  label: {
    type: String,
    default: '',
  },

  labelClass: {
    type: String,
    default: '',
  },

  type: {
    type: String,
    default: 'text',
  },

  tabindex: {
    type: Number,
    default: 0,
  },

  modelValue: {
    type: String,
    default: '',
  },
})

defineEmits(['update:modelValue'])
</script>

<template>
  <label v-if="hasLabel" :class="labelClass">
    <span class="block">
      {{ label }}
    </span>

    <input
      :value="modelValue"
      :type="type"
      class="w-full rounded border border-gray-600 p-1"
      :tabindex="tabindex"
      v-bind="$attrs"
      @input="$emit('update:modelValue', $event.target.value)"
    />
  </label>
</template>
