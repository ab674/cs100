# Abhinav Bassi
# CS 100 2014F Section H03
# TTTP1: Oct 19, 2014

# 1

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.width(2)
t.penup()
t.left(180)
t.forward(150)
t.right(90)
t.forward(50)
t.right(90)
t.pendown()
t.forward(300)
t.penup()
t.left(180)
t.forward(300)
t.left(90)
t.forward(100)
t.left(90)
t.pendown()
t.forward(300)
t.penup()
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.pendown()
t.forward(300)
t.penup()
t.left(180)
t.forward(300)
t.right(90)
t.forward(100)
t.right(90)
t.pendown()
t.forward(300)

# 2

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.width(2)
t.penup()
t.goto(-150, 50)
t.pendown()
t.forward(300)
t.penup()
t.goto(-150,-50)
t.pendown()
t.forward(300)
t.penup()
t.goto(-50,150)
t.right(90)
t.pendown()
t.forward(300)
t.penup()
t.goto(50, 150)
t.pendown()
t.forward(300)

# 3

import turtle 
s = turtle.Screen()
t = turtle.Turtle()
t.width(2)
beginX = [-150, -150, -50, 50]
endX = [150, 150, -50, 50]
beginY = [50, -50, -150, -150]
endY = [50, -50, 150, 150]
t.up()
t.goto(beginX[0],beginY[0])
t.down()
t.goto(endX[0],endY[0])
t.up()
t.goto(beginX[1],beginY[1])
t.down()
t.goto(endX[1],endY[1])
t.up()
t.goto(beginX[2],beginY[2])
t.down()
t.goto(endX[2],endY[2])
t.up()
t.goto(beginX[3],beginY[3])
t.down()
t.goto(endX[3],endY[3])

# 4

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
