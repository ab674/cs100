# Trapdoors & Catapults. A digital version of Chutes & Ladders

# Abhinav Bassi
# CS 100 2014F Section H03
# HW 08: Oct 20, 2014

import random

def getPlayerNames():
    print()
    player1 = input('Name of first player: ')
    player2 = input('Name of second player: ')
    return player1, player2

def getBoardInfo():
    print()
    boardSize = int(input('Number of spaces on the board: '))
    trapdoorNum = int(input('Number of trapdoors: '))
    catapultNum = int(input('Number of catapults: '))
    return boardSize, trapdoorNum, catapultNum

def boardSetup(boardSize, trapdoorNum, catapultNum):
    trapdoors = {}
    catapults = {}
    while len(trapdoors) < trapdoorNum:
        space = random.randint(2, boardSize-1)
        if space in trapdoors:
            continue
        trapdoors[space] = random.randint(1, space-1)
    while len(catapults) < catapultNum:
        space = random.randint(2, boardSize-2)
        if space in trapdoors:
            continue
        if space in catapults:
            continue
        catapults[space] = random.randint(space, boardSize-1)
    return trapdoors, catapults

def rollDie():
    return random.randint(1, 6)

def playGame():
    player1, player2 = getPlayerNames()
    boardSize, trapdoorNum, catapultNum = getBoardInfo()
    trapdoors, catapults = boardSetup(boardSize, trapdoorNum, catapultNum)
    positions = {player1:1, player2:1} 
    player = player1 
    while True:
        print()
        print(player, 'is on', positions[player])
        move = rollDie()
        print(player, 'rolls a', move)
        if positions[player] + move <= boardSize:
            positions[player] += move
            print(player, 'moves to', positions[player])
            if positions[player] == boardSize:
                print(player, 'WINS!')
                break
            if positions[player] in trapdoors:
                positions[player] = trapdoors[positions[player]]
                print('Trapdoor!', player, 'falls to', positions[player])
            elif positions[player] in catapults:
                positions[player] = catapults[positions[player]]
                print('Catapult!', player, 'jumps to', positions[player])               
        else:
            print('Off the board. Sorry, you lose your turn,', player)
        if player == player1:
            player = player2
        elif player == player2:
            player = player1
        
playGame()
