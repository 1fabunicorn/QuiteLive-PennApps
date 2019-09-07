def bitStringAnd(bitString1, bitString2):
    output = ''

    for i in range(len(bitString1)):
        output += str(int(bitString1[i]) and int(bitString2[i]))
    
    return output


def bitStringXor(bitString1, bitString2):
    output = ''

    for i in range(len(bitString1)):
        output += str(int(bitString1[i]) ^ int(bitString2[i]))
    
    return output

def bitStringOr(bitString1, bitString2):
    output = ''

    for i in range(len(bitString1)):
        output += str(int(bitString1[i]) or int(bitString2[i]))
    
    return output



