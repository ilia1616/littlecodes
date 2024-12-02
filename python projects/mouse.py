from graphics import *

def main() :
    win = GraphWin('m',400,400)
    win.setBackground('green')
    ms = Text(Point(win.getWidth()/2,30),'click') 
    ms.setTextColor('red')
    ms.setStyle('bold')
    ms.setSize(15)
    ms.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    
    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    p4 = win.getMouse()
    p4.draw(win)
    
    tr = Polygon(p1,p2,p3,p4)
    tr.setFill('gray')
    tr.setWidth(5)
    tr.setOutline('blue')
    tr.draw(win)
    
main()
