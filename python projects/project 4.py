from graphics import *
from time import sleep

win = GraphWin('page',400,400)
win.setBackground('blue')
a = 1
center = Point (201,201)

p1 = Point(133,133)
p2 = Point(266,133)
p3 = Point(133,266)
p4 = Point(266,266)

re = Polygon(p1,p2,p4,p3)
re.draw(win)
re.setFill('green')

while 1==1:
    p5 = Point(195,270)
    p6 = Point(150,366)
    p7 = Point(240,366)
    p8 = 366

    tr = Polygon(p5,p6,p7)
    tr.setFill('blue')
    tr.setOutline('blue')

    t = Text(center,a)
    t.draw(win)

    while p8 > 130:
        p8 = p8 - 5
        tr.move(0,-5)
        sleep(0.3)
    a += 1
