class Eel {
  get_file_path() {
    return () => '/test-path'
  }

  parse_csv_files(sources) {
    return () => {
      const data = {}
      sources.forEach((source) => {
        const { name, file } = source
        data[name] = { file, columns: ['col1', 'col2', 'col3', 'col4'] }
      })
      return { result: true, data }
    }
  }
}

const eel = new Eel()
