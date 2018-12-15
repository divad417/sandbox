# Import dictionary into list of 'word' objects
f = open('enable1.txt')
allWords = []
for ln in f:
    allWords.append(ln[0:-2])
# Sort words by length
allWords.sort(key=len, reverse=True)
lenWords = [[]]*(len(allWords[0])+1)
# Get indexes of each length
for length in range(2,len(allWords[0])+1):
    lenWords[length] = [a for a in allWords if len(a) == length]
# Search all words
for word in allWords:
    curLen = len(word)
    result = [word]
    if len(result[-1]) == 2:
        print 'Success!'
        break
    for length in reversed(range(curLen)):
        curWord = result[-1]
        left  = [a for a in lenWords[length] if a == curWord[:-1]]
        if left:
            result.append(left[0])
            continue
        right = [a for a in lenWords[length] if a == curWord[1:]]
        if right:
            result.append(right[0])
            continue
        print result
        break
print result