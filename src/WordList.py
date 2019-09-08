import wordswordswords

HexWordLinkList = []


def putZero(str1):
    output = str1[2:]
    return '0x0' + output


for i in range(len(wordswordswords.Words)):
    HexWordLinkList.append([str(hex(i)), wordswordswords.Words[i]])

for i in HexWordLinkList:
    if len(i[0]) == 3:
        i[0] = putZero(i[0])

def WordMapping(Hex, numWords = 32):
    global count

    #Hex length is 64
    count = 0
    output = ''

    for i in range(0, len(Hex), 2):
        for j in HexWordLinkList:
            if Hex[i : i + 2] == j[0][2:]:
                if count < numWords:
                    output += j[1] + ' '
                    count += 1

                  

    return output

print(WordMapping('3b752e632f48f3e8cbf427bda98d69185816c1481f0c775b391b500b0fbd0c54'))

print(count)
