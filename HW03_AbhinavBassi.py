# Abhinav Bassi
# CS 100 2014F Section H03
# HW 03: Sept 19, 2014

# 3.17
print('3.17')
a, b, c = 3, 4, 5
if a<b:
    print('OK')
if c<b:
    print('OK')
if (a+b)==c:
    print('OK')
if ((a**2)+(b**2))==(c**2):
    print('OK')

print(' ')

# 3.18
print('3.18')
a, b, c = 3, 4, 5
if a<b:
    print('OK')
else:
    print('NOT OK')
if c<b:
    print('OK')
else:
    print('NOT OK')
if (a+b)==c:
    print('OK')
else:
    print('NOT OK')
if ((a**2)+(b**2))==(c**2):
    print('OK')
else:
    print('NOT OK')

print(' ')

# Turtle Exercise
color = input('Enter a color: ')
width = int(input('Enter a width: '))
length = int(input('Enter a length: '))
shape = input('Line, triangle or square? ')
import turtle
s = turtle.Screen()
t = turtle.Turtle()
if shape=='Line' or shape=='line':
    t.color(color)
    t.width(width)
    t.forward(length)
    s.exitonclick()
elif shape=='Triangle' or shape=='triangle':
    t.color(color)
    t.width(width)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    s.exitonclick()
elif shape=='Square' or shape=='square':
    t.color(color)
    t.width(width)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    s.exitonclick()
else:
    print('Error')
    s.exitonclick()
