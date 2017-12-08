def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def longest_palindromic(text):   
    g=0
    m=0
    loc=0
    for n in range (0,len(text)):  
        i=1
        for i in range(1,n+1):
            try:
                if text[n-i]==text[n+i] and text[n-i:n+i+1]== reverse(text[n-i:n+i+1]) :
                    g = 0                  
                    if m<i:
                        m=i
                        loc=n
                        i += 1
                elif text[n] == text [n+1]:              
                    g=1
                    if text[n-i]==text[n+g+i]:
                        if m<i:
                            m=i
                            loc=n
                            i +=1                  
            except:
                text[0]         
    return text[loc-m:loc+g+m+1]

print (longest_palindromic("abc"))
