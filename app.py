import eel
from tkinter import filedialog
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2
from venn import venn


@eel.expose
def get_file_path():
    # use the Tkinter file selector because JS can't get full file paths
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    path = filedialog.askopenfilename(filetypes=[('CSV File', '*.csv')])
    return path


@eel.expose
def get_folder_path():
    # use the Tkinter file selector because JS can't get full file paths
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    path = filedialog.askdirectory(mustexist=True)
    return path


@eel.expose
def parse_csv_files(sources):
    sources_dict = {}

    if len(sources) < 2 or len(sources) > 6:
        print(f'Invalid number of sources. Must provide 2-6 sources.')
        return {'result': False, 'error': f'Invalid number of sources. {len(sources)} provided (Min: 2, Max: 6)'}

    for source in sources:
        file = source['file']
        name = source['name']

        try:
            df = pd.read_csv(file, sep=None, engine='python')
            cols = list(df.columns)
            sources_dict[name] = {'file': file, 'columns': cols}

        except Exception as e:
            print(f'There was an error parsing the file at: {file}')
            print(f'ERROR: {str(e)}')
            return {'result': False, 'error': str(e)}

    return {'result': True, 'data': sources_dict}


@eel.expose
def generate_diagram(sources, destination):
    plt.clf()

    if len(sources) < 2 or len(sources) > 6:
        print(f'Invalid number of sources. Must provide 2-6 sources.')
        return {'result': False, 'error': f'Invalid number of sources. {len(sources)} provided (Min: 2, Max: 6)'}

    try:
        dfs = {}
        sets = {}
        all_sources_set = set()

        # create sets for each source and a global set of all sources
        for source in sources:
            pivot = source['pivot']
            name = source['name']
            file = source['file']

            df = pd.read_csv(file, sep=None, engine='python')
            pivot_set = set(df[pivot].dropna())
            all_sources_set = all_sources_set.union(pivot_set)
            sets[name] = pivot_set
            dfs[name] = df

        # generate diagram using appropriate method based on source count
        if len(sources) >= 2 and len(sources) <= 3:
            data = []
            names = []
            for name in sets:
                data.append(sets[name])
                names.append(name)

            if len(sources) == 2:
                venn2(data, names)
            else:
                venn3(data, names)
        else:
            venn(sets)

        # save diagram to destination
        plt.savefig(f'{destination}/venn_diagram.png')

        # create data frame to show where each pivot item is found
        pivot_df = pd.DataFrame(data={'pivot': list(all_sources_set)})

        for source in sources:
            pivot = source['pivot']
            name = source['name']
            pivot_df[f'found_in_{name}'] = pivot_df['pivot'].isin(
                dfs[name][pivot])

        pivot_df.to_csv(f'{destination}/venn_diagram.csv',
                        sep=';', index=False)

        return {'result': True, 'data': None}
    except Exception as e:
        print(f'There was an error generating the diagram.')
        print(f'ERROR: {repr(e)}')
        return {'result': False, 'error': str(e)}


eel.init("web")
eel.start("index.html", port=0)
