import eel
from tkinter import filedialog
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2
from venn import venn

sources_dict = {}
sources_df = {}


@eel.expose
def get_file_path():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    path = filedialog.askopenfilename(filetypes=[('CSV File', '*.csv')])
    return path


@eel.expose
def parse_csv_files(sources):
    for source in sources:
        [file, name] = source
        try:
            df = pd.read_csv(file, sep=None)
            cols = list(df.columns)
            sources_dict[name] = {'file': file, 'columns': cols}
            sources_df[name] = df

        except Exception as e:
            print(f'There was an error parsing the file at: {file}')
            print(f'ERROR: {str(e)}')
            return {'result': False, 'error': str(e)}

    return {'result': True, 'data': sources_dict}


eel.init("web")
eel.start("index.html", port=0)
