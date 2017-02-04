# Abhinav Bassi
# CS 100 2014F Section H03
# HW 07: Oct 19, 2014

# 6.20

def reverse(phonebook):
    d = {}
    for x in phonebook.keys():
        y = phonebook.get(x)
        d[y] = x
    return d

# 6.27

def index(filename, wordList):
    d = {}
    for word in wordList:
        infile = open(filename, 'r')
        lineCount = 1
        foundLine = []
        for line in infile:
            if word in line:
                foundLine.append(lineCount)
            lineCount += 1
        d[word] = foundLine
    infile.close()
    for x in d:
        y = str(d[x])
        print(x, '\t', y.strip('[]'))
