def safe_pawns(pawns):
    alphabet = []
    for letter in range(97,123):
        alphabet.append(chr(letter))
        
    safe = 0
    for position in pawns:
        position =list(position)
        bl=alphabet[alphabet.index(position[0])-1]+str(int(position[1])-1)
        br=alphabet[alphabet.index(position[0])+1]+str(int(position[1])-1)
        
        if bl in pawns and br not in pawns:
            safe+=1
        elif br in pawns and bl not in pawns:
            safe+=1
        elif bl and br in pawns:
            safe +=1       
    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
