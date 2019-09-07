import wordswordswords

HexWordLinkList = []

for i in range(len(wordswordswords.Words)):
    HexWordLinkList.append([hex(i), wordswordswords.Words[i]])


def WordMapping(Hex):

    #Hex length is 64

    output = ''

    for i in range(0, len(Hex), 2):
        for j in HexWordLinkList:
            if j[0] == hex(Hex[i : i + 1]):
                output += j[1] + ", "

    return output

print(WordMapping[''])


