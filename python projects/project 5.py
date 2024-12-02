from tkinter import *
win = Tk()
color = ['red','blue','green','gray','yellow','white']
row_ = 0

for i in color:
    Button(win,text = i,width = 15).grid(row = row_,column = 0)
    Label(win,text = i,bg = i).grid(row = row_,column = 1)
    row_ += 1
