class Eel {
  get_file_path() {
    return () => '/test-path/file.csv'
  }

  get_folder_path() {
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

  generate_diagrams(sources, destination) {
    return () => {
      return { result: true, data: null }
    }
  }
}

const eel = new Eel()
