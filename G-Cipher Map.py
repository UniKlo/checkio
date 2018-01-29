def recall_password(cipher_grille, ciphered_password):

    password=''
    size=len(cipher_grille)
    n=0
    while n<size:
        locs = []
        for index, row in enumerate(cipher_grille):
            if 'X' in row:
                locs.append([index, row.index('X')])
                print ('row.index(\'X\'):',row.index('X'))
                #for i in range (1,size-1) and (row.index('X')+i)<=size:
                try:
                    locs.append([index, row.index('X',(row.index('X')+1))])
                    #looking for 'X' after row.index('X')+1
                    print ()
                    print ("row.index('X',(row.index('X')+1))",row.index('X',(row.index('X')+1)))
                    
                except:
                    pass
    
        print (locs)
        
        for x,y in locs:
            password=password+ ciphered_password[x][y] 
        print (password)   
        cipher_grille=list(zip(*cipher_grille[::-1]))
        #closewise 90 degree
        n+=1

    return password

print (recall_password( ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr'))=='rxqrwsfzxqxzhczy')

'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

    # Rank 2
    assert recall_password(
        ('.X...X.',
         'X.....X',
         '.......',
         '...X...',
         '.......',
         'X.....X',
         '.X...X.'),
        ('loremip',
         'sumdolo',
         'rsitame',
         'tconsec',
         'teturad',
         'ipiscin',
         'gelitqu')) == "oisonineqoisonineqoisonineqoisonineq", "R2"

    # Rank 3
    assert recall_password(
        ('.X...',
         '.X...',
         '..X..',
         '.X...',
         '.X...'),
        ('QWERT',
         'ASDFG',
         'ZXCVB',
         'YUIOP',
         'GHJKL')) == "WSCUHCYUOPRFCOKASFGC", "R3"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
'''