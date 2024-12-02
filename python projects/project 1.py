from graphics import *
from tkinter import *
from time import sleep

win = GraphWin('circle',340,340)
def circle():
    win.setBackground('green')
    p1 = Point(170,170)
    x = 160
    for n in range(1,17):
        c = Circle(p1,x)
        c.draw(win)
        x -= 10
        c.setOutline('red')
        c.setFill('blue')
        c.setWidth(5)
        sleep(0.7)
        
circle()
