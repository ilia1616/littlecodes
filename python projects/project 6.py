from tkinter import *
win = Tk()
win.geometry("400x400")
lb1 = Label(win,text = 'place geometry',bg = 'red')
lb2 = Label(win,text = 'place geometry',bg = 'blue')
lb3 = Label(win,text = 'place geometry',bg = 'yellow')

lb1.place(relx = 0.2,rely = 0.3,relwidth = 0.3,relheight = 0.1)
lb2.place(relx = 0.2,rely = 0.425,relwidth = 0.3,relheight = 0.1)
lb3.place(relx = 0.2,rely = 0.55,relwidth = 0.3,relheight = 0.1)
