print('Loading libraries...')

import eel
from tkinter import filedialog
from tkinter import Tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2
from venn import venn
from openpyxl.workbook.child import INVALID_TITLE_REGEX
import sys
import platform
import logging
import time
import re


@eel.expose
def get_file_path():
    # use the Tkinter file selector because JS can't get full file paths
    # opens the file selector as the topmost window so user can see it
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    # Accept only CSV files
    path = filedialog.askopenfilename(filetypes=[('CSV File', '*.csv')])
    return path


@eel.expose
def get_folder_path():
    # use the Tkinter file selector because JS can't get full file paths
    # opens the file selector as the topmost window so user can see it
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    # Accept only existing directories
    path = filedialog.askdirectory(mustexist=True)
    return path


@eel.expose
def parse_csv_files(sources):
    sources_dict = {}

    # only accept valid number of sources
    if len(sources) < 2 or len(sources) > 6:
        logging.exception(
            f'Invalid number of sources. Must provide 2-6 sources.')
        return {'result': False, 'error': f'Invalid number of sources. {len(sources)} provided (Min: 2, Max: 6)'}

    for source in sources:
        file = source['file']
        name = source['name']

        try:
            # read the source file and save its columns
            df = pd.read_csv(file, sep=None, engine='python')
            cols = list(df.columns)
            sources_dict[name] = {'file': file, 'columns': cols}

        except Exception as e:
            logging.exception(
                f'There was an error parsing the file at: {file}')
            return {'result': False, 'error': str(e)}

    return {'result': True, 'data': sources_dict}


@eel.expose
def generate_diagram(sources, destination):
    # clear diagram, always start with a clean sheet (in case user runs same program multiple times)
    plt.clf()

    # only accept valid number of sources
    if len(sources) < 2 or len(sources) > 6:
        logging.exception(
            f'Invalid number of sources. Must provide 2-6 sources.')
        return {'result': False, 'error': f'Invalid number of sources. {len(sources)} provided (Min: 2, Max: 6)'}

    try:
        timestr = time.strftime("%Y%m%d")
        # initialize excel writer to store the inspection file
        writer = pd.ExcelWriter(
            f'{destination}/venn_diagram_inspect_{timestr}.xlsx', engine='openpyxl')
        dfs = {}
        sets = {}
        all_sources_set = set()

        # create sets for each source and a global set of all sources
        for source in sources:
            pivot = source['pivot']
            name = source['name']
            file = source['file']

            # read the source file (let python figure out which separator it uses)
            df = pd.read_csv(file, sep=None, engine='python')
            # store the source file in the output sheet to facilitate user inspection
            df.to_excel(writer, index=False,
                        sheet_name=re.sub(INVALID_TITLE_REGEX, '_', name))

            # pivot set is a list of unique (lowercased) strings that are not empty
            pivot_set = set(df[pivot].astype(str).str.lower().dropna())
            # join all pivot sets to create the "all sources set"
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
        plt.savefig(f'{destination}/venn_diagram_{timestr}.png')

        # create data frame to show where each pivot item is found
        pivot_df = pd.DataFrame(data={'pivot': list(all_sources_set)})

        for source in sources:
            pivot = source['pivot']
            name = source['name']
            pivot_df[f'found_in_{name}'] = pivot_df['pivot'].isin(
                dfs[name][pivot].astype(str).str.lower())

        pivot_df.to_excel(writer, index=False, sheet_name='Venn Diagram Data')

        writer.close()

        return {'result': True, 'data': None}
    except Exception as e:
        logging.exception(f'There was an error generating the diagram.')
        return {'result': False, 'error': str(e)}


print('Starting local server...')
eel.init("web")
print('Loading application...')

try:
    eel.start("index.html", port=0)
except EnvironmentError:
    # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        eel.start('index.html', mode='edge', port=0)
    else:
        raise

print('App is ready for use')
