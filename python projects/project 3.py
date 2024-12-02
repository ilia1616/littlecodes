from graphics import *
from time import sleep
win = GraphWin('paint',400,400)
win.setBackground('blue')
center = Point(200,100)


a = 1
x = 50

while 1==1:
    p1 = Point(200.0, 220.0)
    p2 = Point(280.0, 400.0)
    p3 = Point(120.0, 400.0)
    p4 = 220
    ci = Circle(center,50)
    ci.draw(win)

    po = Polygon(p1,p2,p3)
    po.draw(win)
                 
    po.setWidth(3)
    ci.setWidth(3)
    
    po.setFill('green')
    ci.setFill('red')
    
    t = Text(center,a)
    t.draw(win)
    while p4 > x:
        po.move(0,-5)
        p4 = p4 - 5
        sleep(0.3)
    a = a + 1

