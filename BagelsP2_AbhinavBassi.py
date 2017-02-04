# Abhinav Bassi

# Problem 2

# Credit: Rahul Syal and Taylor Tu

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
    guess = getGuess()
    return getClues(secret, guess)

def getPossibleGuesses(guessHistory, clueHistory):
    possNums = []
    for i in range(len(guessHistory)):
        guess = guessHistory[i]
        clue = clueHistory[i]
        for i in range(10,1000):
            secret = ''
            if (i < 100):
                secret += '0' + str(i)
            else:
                secret += str(i)
            if secret[0] == secret[1] or secret[0] == secret[2] or secret[1] == secret[2]:
                continue
            if getClues(secret, guess) == clue:
                possNums.append(secret)
    actualPoss = []
    for x in range(len(possNums)):
        if possNums.count(possNums[x]) == len(guessHistory) and possNums[x] not in actualPoss:
            actualPoss.append(possNums[x])
    return actualPoss

def bagelsPlayer2(guessHistory, clueHistory):
    guessList = getPossibleGuesses(guessHistory, clueHistory)
    low = 720
    educGuess = ''
    for guess in guessList:
        gMaxDict = {}
        gMax = 0
        for secret in guessList:
            clue = tuple(getClues(secret, guess))
            if clue not in gMaxDict:
                gMaxDict[clue] = 1
            else:
                gMaxDict[clue] += 1
        for g in gMaxDict:
            gMax = max(gMaxDict[g], gMax)
        if gMax < low:
            low = min(gMax, low)
            educGuess = guess
    return educGuess

total = 0
loops = 0
clueHistory = []
guessHistory = []
secret = generateSecret()
print('Secret number: ', secret)
guess = '012'
loops += 1
guessHistory.append(guess)
while secret != guess:
    clues = getClues(secret, guess)
    clueHistory.append(clues)
    guess = bagelsPlayer2(guessHistory, clueHistory)
    guessHistory.append(guess)
    loops += 1
total += loops
print('You got it! Number of guesses: ', total)

##count = 0
##for i in range(100):
##    total = 0
##    loops = 0
##    clueHistory = []
##    guessHistory = []
##    secret = generateSecret()
##    guess = '012'
##    loops += 1
##    guessHistory.append(guess)
##    while secret != guess:
##        clues = getClues(secret, guess)
##        clueHistory.append(clues)
##        guess = bagelsPlayer2(guessHistory, clueHistory)
##        guessHistory.append(guess)
##        loops += 1
##    total += loops
##    count += total
##    print('Trial ', i+1)
##print('Average number of guesses: ', count/100)
