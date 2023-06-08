<script setup>
import { ref } from 'vue'
import StepOne from './components/step-one/StepOne.vue'

const step = ref(1)
const sourceCount = ref(3)
</script>

<template>
  <div class="p-4">
    <StepOne v-if="step === 1" :source-count="sourceCount" />
  </div>
</template>
