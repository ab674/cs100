# Abhinav Bassi
# CS 100 2014F Section H03
# HW 09: Nov 12, 2014

# 6.20

def reverse(phonebook):
    d = {}
    for x in phonebook.keys():
        y = phonebook.get(x)
        d[y] = x
    return d

# 6.21

def ticker(filename):
    name = input('Company Name: ')
    infile = open(filename, 'r')
    line = infile.readline()
    ticker = ''
    while line:
        if line.strip() == name.title():
            ticker = infile.readline().strip()
            break
        else:
            line = infile.readline()
    if ticker:
        print('Ticker: ' + ticker)
    else:
        print ('Error')

# 6.22

def mirror(word):
    criteria = 'bdopqvwx'
    mirrored = {'b':'d','d':'b','o':'o','p':'q','q':'p','v':'v','w':'w','x':'x'}
    mirrorWord = ''
    for x in word:
        if x not in criteria:
            print('INVALID!')
            flag = 1
            break
        else:
            mirrorWord += mirrored[x]
    if flag != 1:
        print(mirrorWord[::-1])

# 6.23

import string
def scaryDict(filename):
    infile = open(filename,'r')
    lines = infile.read()
    line = lines.split()
    d = {}
    sortedList = []
    for x in line:
        x = x.strip(string.punctuation)
        if len(x) > 2:
            sortedList.append(x)
    sortedList.sort()
    for y in sortedList:
        print(y, end = '\n')
