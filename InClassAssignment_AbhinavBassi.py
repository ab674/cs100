def wordStats(fileName):
    infile = open(fileName, 'r')
    content = infile.read()
    contentList = content.split()
    d = {}
    uniqueWords = []
    lengthList = []
    for word in contentList:
        if word not in uniqueWords:
            uniqueWords.append(word)
    for word in uniqueWords:
        if len(word) not in lengthList:
            lengthList.append(len(word))
    for length in lengthList:
        criteriaList = []
        for word in uniqueWords:
            if len(word) == length:
                criteriaList.append(word)
        d[length] = criteriaList
    infile.close()
    return d
