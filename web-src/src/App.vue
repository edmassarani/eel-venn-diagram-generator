<script setup>
import { storeToRefs } from 'pinia'
import { useSourceStore } from '@/stores/SourceStore'
import StepOne from './components/step-one/StepOne.vue'
import TextButton from '@utils/TextButton.vue'

const store = useSourceStore()

const { sourceCount, step } = storeToRefs(store)

const proceed = () => {
  store.advanceStep()
}

const goBack = () => {
  store.retreatStep()
}
</script>

<template>
  <form
    class="flex max-h-screen flex-col overflow-hidden p-4"
    @submit.prevent="proceed"
  >
    <StepOne v-if="step === 0" :source-count="sourceCount" />

    <text-button type="submit">Continue</text-button>
    <text-button v-if="step > 0" @click="goBack">Go Back</text-button>
  </form>
</template>
