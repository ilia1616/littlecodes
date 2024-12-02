from tkinter import *
from graphics import *
a1 = input('hello my friend. what is your name? ')
print('hi ' + a1)
a2 = input('if you like calculat press c and if you like paint press p and next enter ' + a1 + ' :')
if a2=='c':
    print('first>second')
    num1 = input('please enter first number ' + a1 + ' :')
    num2 = input('please enter second number ' + a1 + ' :')
    print('a to add__+')
    print('s to subrication__-')
    print('m to multiplication__×')
    print('d to division__÷')
    print('p to power__**')
    print('r to root__//')
    print('a to average')
    a3 = input('')
    if a3=='a':
        num3 = int(num1) + int(num2)
        print(num3)
    if a3=='s':
        num3 = int(num1) - int(num2)
        print(num3)
    if a3 == 'm':
        num3 = int(num1) * int(num2)
        print(num3)
    if a3 == 'd':
        num3 = int(num1) / int(num2)
        print(num3)
    if a3 == 'p':
        num3 = int(num1) ** int(num2)
        print(num3)
    if a3 == 'r':
        num3 = int(num1) // int(num2)
        print(num3)
    if a3 == 'a':
        num3 = (int(num1) + int(num2)) / 2
        print(num3)
if a2 == 'p':
    win = GraphWin('paint',300,300)
    win
    print('c to circle')
    print('r torectangle')
    print('s to squar')
    print('l to line')
    print('o to oval')
    a3 = input('')
    p1 = Point(150,150)
    p2 = Point(180,200)
    if a3 == 'c':
        cl = Circle(p1,50)
        cl.draw(win)
    if a3 == 'r':
        r = Rectangle(p1,p2)
        r.draw(win)
    if a3 == 's':
        sq = Rectangle(Point(100,100),Point(150,150))
        sq.draw(win)
    if a3 == 'l':
        li = Line(p1,p2)
        li.draw(win)
    if a3 == 'o':
        o = Oval(p1,p2)
        o.draw(win)
    sh = input('which shape you want to fill it? (just one word  example(o = oval) ) ')
    co = input('what color you want for your shape? ')
    if sh == 'c':
        cl.setFill(co)
    if sh == 'r':
        r.setFill(co)
    if sh == 's':
        sq.setFill(co)
    if sh == 'o':
        o.setFill(co)
