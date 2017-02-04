# Abhinav Bassi
# CS 100 2014F Section H03
# HW 06: Oct 12, 2014

# 4.27

def fcopy(fileName1, fileName2):
    infile = open(fileName1, 'r')
    outfile = open(fileName2, 'w')
    content = infile.read()
    outfile.write(content)
    infile.close()
    outfile.close()

# 4.29

def stats(fileName):
    infile = open(fileName, 'r')
    content = infile.read()
    wordList = content.split()
    infile.close()
    print('Line count: ', content.count('\n'))
    print('Word count: ', len(wordList))
    print('Character count: ', len(content))

# HW Problem 3

def repeatWords(filename1, filename2):
    import string
    infile = open(filename1, 'r')
    outfile = open(filename2, 'w')
    for line in infile:
        tempList = []
        repeatedWordsList = []
        repeatedWords = ''
        repeatedWordsFinal = ''
        content = line.lower()
        textList = content.split()
        for word in textList:
            tempList.append(word.strip(string.punctuation))
        for x in tempList:
            if tempList.count(x) > 1:
                word = x
                if word not in repeatedWordsList:
                    repeatedWordsList.append(word)
                    repeatedWords += (word + ' ')
                    repeatedWordsFinal = repeatedWords + '\n'
        outfile.write(repeatedWordsFinal)
