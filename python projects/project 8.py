from tkinter import *
from tkinter.filedialog import askopenfilename

def callback():
    name = askopenfilename (filetype = (('application file','*.exe'),('all files','*.*')))
    print(name)
callback()
