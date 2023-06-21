<script setup>
import { storeToRefs } from 'pinia'
import { useSourceStore } from '@/stores/SourceStore'
import StepOne from './components/step-one/StepOne.vue'
import StepTwo from './components/step-two/StepTwo.vue'
import TextButton from '@utils/TextButton.vue'
import { watch } from 'vue'

const store = useSourceStore()

const { step, sources, destinationPath } = storeToRefs(store)

const proceed = () => {
  store.advanceStep()
}

const goBack = () => {
  store.retreatStep()
}

watch(step, async (newStep, oldStep) => {
  if (oldStep < newStep) {
    // trigger functions on step increase (starts at 0)
    switch (newStep) {
      case 1: {
        // eslint-disable-next-line no-undef
        const res = await eel.parse_csv_files(sources.value)()

        if (!res.result) {
          alert(res.error)
          goBack()
        } else {
          sources.value.forEach((source) => {
            source.columns = res.data[source.name].columns
          })
        }

        break
      }

      case 2: {
        // eslint-disable-next-line no-undef
        const res = await eel.generate_diagrams(
          sources.value,
          destinationPath
        )()

        if (!res.result) {
          alert(res.error)
          goBack()
        } else {
          sources.value.forEach((source) => {
            source.columns = res.data[source.name].columns
          })
        }

        break
      }

      default:
        break
    }
  }
})
</script>

<template>
  <form
    class="flex max-h-screen flex-col overflow-hidden p-4"
    @submit.prevent="proceed"
  >
    <StepOne v-if="step === 0" />
    <StepTwo v-else-if="step === 1" />

    <text-button type="submit"> Continue </text-button>
    <text-button v-if="step > 0" class="mt-2" @click="goBack">
      Go Back
    </text-button>
  </form>
</template>
