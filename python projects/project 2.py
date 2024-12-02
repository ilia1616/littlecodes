from tkinter import *
from tkinter import messagebox

win = Tk()
m = Menu(win,tearoff = 0)
win.config(menu = m)
f = Menu(m)
fm = Menu(m,tearoff = 0)
def noting():
    pass

fm.add_command(label = 'new',command = noting)
fm.add_command(label = 'open',command = noting)

fm.add_separator()
fm.add_command(label = 'exit',command = win.destroy)
m.add_cascade(label = 'file',menu = fm)

re = Menu(m,tearoff =0)
re.add_command(label = 'cut',command = noting)
fm.add_cascade(label = 'rscent',menu = re)
