import eel
from tkinter import filedialog
from tkinter import *


@eel.expose
def get_file_path():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    path = filedialog.askopenfilename(filetypes=[('CSV File', '*.csv')])
    return path


eel.init("web")
eel.start("index.html", port=0)
