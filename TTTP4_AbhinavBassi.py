# Abhinav Bassi
# CS 100 2014F Section H03
# TTTP4: Nov 20, 2014

# 1

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
coordinateList = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
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

def tttPlayGame():
    import turtle
    s = turtle.Screen()
    pen = turtle.Turtle()
    drawGrid(pen,100,-150,-150)
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# 3

triplets = [[board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[0][2]]]

# 4

def xWin(triplets):
    flag = False
    for winningCombination in triplets:
        if winningCombination[0] == 'X' and winningCombination[1] == 'X' and winningCombination[2] == 'X':
            flag = True
    return flag

# 5

def oWin(triplets):
    flag = False
    for winningCombination in triplets:
        if winningCombination[0] == 'O' and winningCombination[1] == 'O' and winningCombination[2] == 'O':
            flag = True
    return flag
