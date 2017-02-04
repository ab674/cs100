# Abhinav Bassi
# CS 100 2014F Section H03
# HW 02: Sept 17, 2014

# 2.23
print('2.23')
lst=[3,7,-2,12]
print('List: ', lst)
lst.sort()
lstrange = lst[-1]-lst[0]
print('Range = ', lstrange)

print(' ')

# 2.25
print('2.25')
0==(1==2)
print('0==(1==2)')
print('First, Python checks the expression 1==2. Since this is false, the corresponding value is 0. Then Python checks the expression 0==0, which is true.')
2+(3==4)+5==7
print('2+(3==4)+5==7')
print('First, Python checks the expression 3==4. Since this is false, the corresponding value is 0. Then Python adds 2+0+5, which is 7, and check the expression 7==7, which is true.')
(1<-1)==(3>4)
print('(1<-1)==(3>4)')
print('First, Python checks the expressions 1<-1 and 3>4. Since both are false, the corresponding values are both 0. Then Python checks the expression 0==0, which is true.')

# 2.26
import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
s.exitonclick()
# I used s.exitonclick() instead of the book directions so that you could see the square before the screen was deleted

# 2.27
s = turtle.Screen()
t = turtle.Turtle()
t.left(60)
t.forward(100)
t.right(120)
t.forward(100)
t.right(60)
t.forward(100)
t.right(120)
t.forward(100)
t.right(60)
s.exitonclick()

# 2.30
s = turtle.Screen()
t = turtle.Turtle()
t.circle(50)
t.penup()
t.sety(10)
t.pendown()
t.circle(40)
t.penup()
t.sety(20)
t.pendown()
t.circle(30)
t.penup()
t.sety(30)
t.pendown()
t.circle(20)
s.exitonclick()
