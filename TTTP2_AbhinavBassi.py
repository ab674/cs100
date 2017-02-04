# Abhinav Bassi
# CS 100 2014F Section H03
# TTTP2: Oct 22, 2014

# 1

def tttDrawMove(t, row, col, mark, edge):
    buffer =  (.2*edge)
    newEdge = edge - (2*buffer)
    t.up()
    t.width(1)
    t.goto(0,0)
    if row == 0:
        y = -((3/2)*edge)
    elif row == 1:
        y = -((1/2)*edge)
    elif row == 2:
        y = ((1/2)*edge)
    if col == 0:
        x = 0-edge
    elif col == 1:
        x = 0
    elif col == 2:
        x = 0+edge
    t.goto(x,y)
    if mark =='x' or mark == 'X':
        t.up()
        t.setheading(0)
        t.forward(newEdge/2)
        t.left(90)
        t.forward(buffer)
        t.setheading(0)
        t.left(135)
        t.down()
        t.forward(math.sqrt((newEdge**2)+(newEdge**2)))
        t.up()
        t.setheading(0)
        t.forward(newEdge)
        t.right(135)
        t.down()
        t.forward(math.sqrt((newEdge**2)+(newEdge**2)))
        t.up()
        t.setheading(0)
        t.goto(0,0)
    if mark =='o' or mark == 'O':
        t.up()
        t.setheading(0)
        t.left(90)
        t.forward(buffer)
        t.setheading(0)
        t.down()
        t.circle(newEdge/2)
        t.up()
        t.setheading(0)
        t.goto(0,0)

# 2

def drawGrid(t, length, x, y):
    t.width(2)
    beginX = [x, x, x+length, x+(2*length)]
    endX = [x+(3*length), x+(3*length), x+(length), x+(2*length)]
    beginY = [y+(2*length), y+length, y, y]
    endY = [y+(2*length), y+length, y+(3*length), y+(3*length)]
    for i in range(4):
        t.up()
        t.goto(beginX[i],beginY[i])
        t.down()
        t.goto(endX[i],endY[i])

import turtle
s = turtle.Screen()
pen = turtle.Turtle()
drawGrid(pen,100,-150,-150)

import math
tttDrawMove(pen, 0, 0, 'X', 100)
tttDrawMove(pen, 0, 1, 'X', 100)
tttDrawMove(pen, 0, 2, 'X', 100)
tttDrawMove(pen, 1, 0, 'O', 100)
tttDrawMove(pen, 1, 1, 'O', 100)
tttDrawMove(pen, 1, 2, 'O', 100)
