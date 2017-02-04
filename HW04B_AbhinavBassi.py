# Abhinav Bassi
# CS 100 2014F Section H03
# HW 04B: Sept 24, 2014

# Question 11A
def parallelLines(numLines, lineLength):
    for x in range(1,numLines+1):
        t.forward(lineLength)
        t.penup()
        t.goto(0,-(x*25))
        t.pendown()

# Question 11B
import turtle
s = turtle.Screen()
t = turtle.Turtle()
parallelLines(5, 100)
s.exitonclick()

# Question 12A
def containsLetter(aLetter, strList):
    foundLetter=[]
    for x in strList:
        if aLetter in x:
            foundLetter.append(x)
    return(foundLetter)

# Question 12B
hulkLine = ["you", "wouldn't", "like", "me", "when", "i'm", "angry"]
for x in "hulk":
    print(containsLetter(x,hulkLine))

# Question 13A
def getInt(minInt, maxInt):
    userNum = int(input('Please give me a number no less than '+ str(minInt) + ' and no greater than ' + str(maxInt) + ': '))
    print(userNum)
    
# Question 13B
def getNumber(minInt, maxInt):
    userNum = int(input('Please give me a number no less than '+ str(minInt) + ' and no greater than ' + str(maxInt) + ': '))
    if userNum==0:
        print(userNum, ': Zero')
    elif userNum>0:
        print(userNum, ': Positive')
    else:
        print(userNum, ': Negative')
