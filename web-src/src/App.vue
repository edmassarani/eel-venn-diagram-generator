<script setup>
import { storeToRefs } from 'pinia'
import { watch } from 'vue'
import { mdiCheckCircleOutline } from '@mdi/js'
import SvgIcon from '@jamescoyle/vue-icon'
import { useSourceStore } from '@/stores/SourceStore'
import StepOne from './components/step-one/StepOne.vue'
import StepTwo from './components/step-two/StepTwo.vue'
import TextButton from '@utils/TextButton.vue'

const store = useSourceStore()

const { step, sources, destinationPath } = storeToRefs(store)

const proceed = () => {
  store.advanceStep()
}

const goBack = () => {
  store.retreatStep()
}

const resetStore = () => {
  store.$reset()
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
        const res = await eel.generate_diagram(sources.value, destinationPath)()

        if (!res.result) {
          goBack()
          alert(res.error)
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
    <div
      v-if="step === 2"
      class="flex h-[50vh] flex-col items-center justify-center text-center"
    >
      <svg-icon
        type="mdi"
        :path="mdiCheckCircleOutline"
        size="100"
        class="text-green-600"
      ></svg-icon>
      <p>Your files have been created and stored successfully.</p>
      <p>You can now restart the process or close this application.</p>
    </div>

    <text-button v-if="step < 2" type="submit"> Continue </text-button>
    <text-button v-if="step > 0" class="my-2" @click="goBack">
      Go Back
    </text-button>
    <text-button v-if="step > 0" type="button" @click="resetStore">
      Restart
    </text-button>
  </form>
</template>
