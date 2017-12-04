def checkio(matrix):
    l=len(matrix)
    for row in matrix:
        for i in range (0,l-3):        
            if row[i]==row[i+1]==row[i+2]==row[i+3]:       
                return True        

    rotated_field = list(zip(*matrix))
    
    for row in rotated_field: 
        for i in range (0,l-3):        
            if row[i]==row[i+1]==row[i+2]==row[i+3]:
                return True

    for ro in range (0,l-3):
        for co in range (0,l-3):
            if (matrix [ro][co])==(matrix [ro+1][co+1])==(matrix [ro+2][co+2])==(matrix [ro+3][co+3]):
                    return True
            
    for ro in range (0,l-3):
        for co in range (l-3,l):
            if (matrix [ro][co])==(matrix [ro+1][co-1])==(matrix [ro+2][co-2])==(matrix [ro+3][co-3]):
                return True
    return False

print (checkio([[2,3,6,5,6,2,8,3,7,4],[6,9,5,9,7,6,8,5,1,6],[6,8,2,6,1,9,3,6,6,4],[5,8,3,2,3,8,7,4,6,4],[2,3,1,4,5,1,2,5,6,9],[5,4,8,7,5,5,8,4,9,5],[9,7,9,9,5,9,9,8,1,2],[5,1,7,4,8,3,4,1,8,8],[5,3,3,2,6,1,4,3,8,8],[4,8,1,4,5,8,8,7,4,7]]))

# https://py.checkio.org/mission/find-sequence/