VOWELS = ('a','e','i','o','u','y')

def translate(phrase):
    lst=list(phrase)
    for i in range (0,len(lst)):
        try:
            if lst[i] not in VOWELS and lst[i].isalpha() is True:
                del lst[i+1]
        except:
            pass
  
    for i in range (0,len(lst)):
        try:
            if lst[i] in VOWELS and lst[i]==lst[i+1]==lst[i+2]:            
                del lst[i],lst[i+1]              
        except:
            pass      

    return ''.join(lst)
   
    
print (translate("hoooowe yyyooouuu duoooiiine"))