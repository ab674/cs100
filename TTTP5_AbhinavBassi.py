# Abhinav Bassi
# CS 100 2014F Section H03
# TTTP5: Dec 5, 2014

# 1

triplets = [[board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[0][2]]]

def isDraw(triplets):
    flag = False
    count = 0
    for possibleCombination in triplets:
        if 'X' in possibleCombination and 'O' in possibleCombination:
            count += 1
        if count == 8:
            flag = True
    return flag

# Full Game

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

def tttGetMove():
    x = int(input('Enter x coordinate: '))
    xList = ['0', '1', '2']
    while str(x) not in xList:
        x = int(input('Invalid coordinate. Enter x coordinate: '))
    y = int(input('Enter y coordinate: '))
    yList = ['0', '1', '2']
    while str(y) not in yList:
        y = int(input('Invalid coordinate. Enter y coordinate: '))
    coordinate = (str(x)+str(y))
    return coordinate

def tttComputerMove():
    import random
    x = random.randint(0,2)
    y = random.randint(0,2)
    coordinate = (str(x)+str(y))
    return coordinate

def moveValidation():
    userCoordinate = tttGetMove()
    while userCoordinate not in coordinateList:
        print('Invalid move.')
        userCoordinate = tttGetMove()
    coordinateList.remove(userCoordinate)
    if len(coordinateList) != 0:
        formattedCoordinate = ('(' + userCoordinate[0] + ',' + userCoordinate[-1] + ')')
        return formattedCoordinate
    else:
        message = 'No more possible moves.'
        return message

def xWin(triplets):
    flag = False
    for winningCombination in triplets:
        if winningCombination[0] == 'X' and winningCombination[1] == 'X' and winningCombination[2] == 'X':
            flag = True
    return flag

def oWin(triplets):
    flag = False
    for winningCombination in triplets:
        if winningCombination[0] == 'O' and winningCombination[1] == 'O' and winningCombination[2] == 'O':
            flag = True
    return flag

def isDraw(triplets):
    flag = False
    count = 0
    for possibleCombination in triplets:
        if 'X' in possibleCombination and 'O' in possibleCombination:
            count += 1
        if count == 8:
            flag = True
    return flag

def tttPlayGame():
    import turtle
    s = turtle.Screen()
    pen = turtle.Turtle()
    drawGrid(pen,100,-150,-150)
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    coordinateList = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    triplets = [[board[0][0], board[0][1], board[0][2]],
                [board[1][0], board[1][1], board[1][2]],
                [board[2][0], board[2][1], board[2][2]],
                [board[0][0], board[1][0], board[2][0]],
                [board[0][1], board[1][1], board[2][1]],
                [board[0][2], board[1][2], board[2][2]],
                [board[0][0], board[1][1], board[2][2]],
                [board[0][2], board[1][1], board[0][2]]]

while True:
    tttPlayGame()
    userChoice = input('Type \'Yes\' to play again or \'Quit\' to quit.')
    if userChoice == 'Quit':
        break
    elif userChoice == 'Yes':
        pen.clear()
        tttPlayGame()
    else:
        userChoice = input('Type \'Yes\' to play again or \'Quit\' to quit.')
