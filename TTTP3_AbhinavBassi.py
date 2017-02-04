# Abhinav Bassi
# CS 100 2014F Section H03
# TTTP3: Nov 5, 2014

# 2

def tttGetMove():
    x = int(input('Enter x coordinate: '))
    xList = ['0', '1', '2']
    while str(x) not in xList:
        x = int(input('Invalid coordinate. Enter x coordinate: '))
    y = int(input('Enter y coordinate: '))
    yList = ['0', '1', '2']
    while str(y) not in yList:
        y = int(input('Invalid coordinate. Enter y coordinate: '))
    coordinate = (x, y)
    return coordinate

# 3

for i in range(6):
    print(tttGetMove())
