<script setup>
import { ref } from 'vue';
import StepOne from './components/step-one/index.vue';

const step = ref(1);
</script>

<template>
  <div class="p-4">
    <StepOne v-if="step === 1" />
  </div>
</template>
