import { defineStore } from 'pinia'

export const useSourceStore = defineStore('sources', {
  state: () => ({
    sources: [
      { name: '', file: '' },
      { name: '', file: '' },
    ],
    destinationPath: '',
    minCount: 2,
    maxCount: 6,
    step: 0,
    loading: false,
  }),

  getters: {
    sourceCount(state) {
      return state.sources.length
    },

    isAtMaxCapacity(state) {
      return state.sourceCount >= state.maxCount
    },

    isAtMinCapacity(state) {
      return state.sourceCount <= state.minCount
    },
  },

  actions: {
    addSource() {
      if (this.sourceCount < this.maxCount) {
        this.sources.push({ name: '', file: '' })
        return true
      }

      return false
    },

    removeSource(index) {
      if (this.sourceCount > this.minCount) {
        this.sources.splice(index, 1)
        return true
      }

      return false
    },

    setSourceName(index, name) {
      this.sources[index].name = name
    },

    setSourceFile(index, file) {
      this.sources[index].file = file
    },

    setSourcePivotColumn(index, column) {
      this.sources[index].pivot = column
    },

    setDestinationPath(path) {
      this.destinationPath = path
    },

    advanceStep() {
      this.step++
    },

    retreatStep() {
      this.step--
    },
  },
})
