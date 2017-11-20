def checkio(number):
     strnum=str(number)
     c=1
     n=0
   
     while n < len(strnum):
         if int(strnum[n])==0:
             c=c*1
         else:
             c=c*int(strnum[n])      
         n+=1        
     return c

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
