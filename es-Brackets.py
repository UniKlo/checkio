def checkio(str):
    if str:
        brackets = [ ('(',')'), ('[',']'), ('{','}')]
        # define fake constants - python does not support the concept of constants
        kStart = 0
        kEnd = 1

        # internal stack used to push and pop brakets in the input string
        stack = []

        for char in str:
            for bracketPair in brackets:
                if char == bracketPair[kStart]:
                    stack.append(char)
                  
              #  if char == bracketPair[kEnd] and len(stack) == 0 and stack.pop() != bracketPair[kStart]:
                elif char == bracketPair[kEnd] and (len(stack) == 0 or stack.pop() != bracketPair[kStart]):
                    return False
        print (stack.pop() )
        print (bracketPair[kEnd])
        print (stack)
        if len(stack) == 0:
            return True
    return False
print (checkio("(((1+(1+1))))]"))
    
    
'''
    stack = []
    stackr = []
    pushChars, popChars = "<({[", ">)}]"
    for c in str :
        if c in pushChars :
            stack.append(c)
        if c in popChars:
            stackr.append(c)
            
    print (stack) 
    stackr = stackr.reverse()
    print (stackr)
    if stack == stackr.reverse():
 
        
        return True
    else :
     
        return False
                   
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
'''