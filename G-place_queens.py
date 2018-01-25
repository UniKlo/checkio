def place_queens(placed):
    alphabet = []
    for letter in range(97,105):
        alphabet.append(chr(letter))
 
    sumban=[]
    print (type(placed),placed)
    
    for position in placed:
        banned=[]
        
        print ('position',position)
        positionlst =list(position)
        
        for abc in alphabet:
            banned.append(abc+positionlst[1])
            while position in banned:
                banned.remove(position)
        print ('position:',position,banned,len(banned),'\n')
        
        for i in range (1,9):
            banned.append(positionlst[0]+str(i))
            while position in banned:
                banned.remove(position)
        print ('position:',position,banned,len(banned),'\n')
        
        
        #Right,Bottom area
        ina=alphabet.index(positionlst[0])
        #range (0-7)        
        in8=int(positionlst[1])
        #range(1-8) 
        while ina<7 and in8>1:
            almoveup=alphabet[ina+1]
            nummovedown=str(in8-1)
            banned.append(almoveup+nummovedown)
            ina=ina+1
            in8=in8-1
            
        #Left,Bottom area        
        ina=alphabet.index(positionlst[0])       
        in8=int(positionlst[1])
        while ina>0 and in8>1:
            almovedown=alphabet[ina-1]
            nummovedown=str(in8-1)
            banned.append(almovedown+nummovedown)
            ina=ina-1
            in8=in8-1
            
        #Left,upper area        
        ina=alphabet.index(positionlst[0])       
        in8=int(positionlst[1])
        while ina>0 and in8<8:
            almovedown=alphabet[ina-1]
            nummoveup=str(in8+1)
            banned.append(almovedown+nummoveup)
            ina=ina-1
            in8=in8+1
        
        #Right,up area
        ina=alphabet.index(positionlst[0])     
        in8=int(positionlst[1])
        while ina<7 and in8<8:
            almoveup=alphabet[ina+1]
            nummoveup=str(in8+1)
            banned.append(almoveup+nummoveup)
            ina=ina+1
            in8=in8+1
            
        sumban=sumban+banned

    print (sumban,len(sumban))
    ans=set(placed).issubset(set(sumban))
    return not ans

print (place_queens({"b2", "c4", "d6", "e8", "a7", "g5"}))
            




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations

    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
        for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example"
    assert checker(place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, True), "2nd Example"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
