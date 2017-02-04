# Abhinav Bassi

# Problem 1

import random

def generateSecret():
    randNum = ''
    digitCount = 0
    while digitCount < 3:
        digit = random.randint(0,9)
        if str(digit) not in randNum:
            randNum += str(digit)
            digitCount += 1
    return randNum

def getGuess():
    userint = input('Your three digit guess please: ')
    while len(userint) != 3:
        userint = input('Your three digit guess please: ')
    return userint

def getClues(secret, guess):
    secretList = []
    for x in secret:
        secretList.append(x)
    guessList = []
    for y in guess:
        guessList.append(y)
    fermis = 0
    for i in range(3):
        if secretList[i] == guessList[i]:
            fermis += 1
    bagels = 0
    for j in range(3):
        if guessList[j] not in secret:
            bagels += 1
    picos = 3-(fermis+bagels)
    return bagels, picos, fermis

def playBagelsPlayer1():
    secret = generateSecret()
    loops = 1
    masterGuessList = []
    masterClueList = []
    while True:
        guess = getGuess()
        masterGuessList.append(guess)
        clues = getClues(secret, guess)
        masterClueList.append(clues)
        print('Your clues: bagels ' + str(clues[0]) + ' picos ' + str(clues[1]) + ' fermis ' + str(clues[2]))
        if guess == secret:
            print('You got it! Number of guesses: ' + str(loops))
            break
        loops += 1

playBagelsPlayer1()
