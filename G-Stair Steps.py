def golf(numbers):
    total = sum(numbers)
    
    i=0 
    while i <len(numbers):
        sublist=[]
        try:
            while numbers[i]<0: 
                
                sublist.append(numbers[i])
                i+=1
        except:
            pass
        i+=1
        
        #print ("i:",i,"sublist:",sublist) 
       
        if len(sublist) ==1:
            total= total-sum(sublist)
            
        elif len(sublist)>1:
            n=1
            opt1=[]
            opt2=[]
            while n < (len(sublist)+1):
                if n%2!=0:
                    opt1.append(sublist[n-1])
                else:
                    opt2.append(sublist[n-1])
                n+=1
        
            op=0
            oplist=[]
            while op <len(sublist)-1:
                oplist.append(min(sublist[op],sublist[op+1]))
                op+=2
            
            for a in range (len(oplist)-1):
                if numbers.index(oplist[a])+1== numbers.index(oplist[a+1]):
                    oplist=[]

            #print ("opt1:",opt1,"opt2:",opt2,"oplist:",oplist) 
            total=total-min(sum(opt1),sum(opt2),sum(oplist))   


    return total
    


if __name__ == '__main__':
     # These "asserts" using only for self-checking and not necessary for auto-testing
     assert golf((5, -3, -1, 2)) == 6
     assert golf((5, 6, -10, -7, 4)) == 8
     assert golf((-11, 69, 77, -51, 23, 67, 35, 27, -25, 95)) == 393
     assert golf((-21, -23, -69, -67, 1, 41, 97, 49, 27)) == 125
     print("Use 'Check' to earn sweet rewards!")
