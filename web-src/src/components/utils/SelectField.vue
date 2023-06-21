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

  tabindex: {
    type: Number,
    default: 0,
  },

  modelValue: {
    type: String,
    default: '',
  },

  options: {
    type: Array,
    required: true,
  },
})

defineEmits(['update:modelValue'])
</script>

<template>
  <label v-if="hasLabel" :class="labelClass">
    <span class="block">
      {{ label }}
    </span>

    <select
      :value="modelValue"
      class="w-full rounded border border-gray-600 p-1"
      :tabindex="tabindex"
      v-bind="$attrs"
      @input="$emit('update:modelValue', $event.target.value)"
    >
      <option v-for="option of options" :key="option" :value="option">
        {{ option }}
      </option>
    </select>
  </label>
</template>
