
def find_word(text, word):
    text = text.replace(" ","")
    text = text.split("\n")
    
    #print (text)
    
    locations=[]
    location=[]
    
    for row in text:
        row=row.lower()
        #print (row)
        locations.append(row.find(word)+1)
    #print ('locations: ',locations)
    
    if all (loc ==0 for loc in locations) is True:
        LOC=[]
        rotated90 = list(zip(*text[::-1]))            
        
        for line in rotated90:
            line="".join(line)
            print (line)
            line=line.lower()
            LOC.append(line.find(word[::-1])+1)
        #print (LOC)    
        for loc1 in LOC:
            #print (LOC.index(loc1))
            if loc1 > 0:
                location.append(abs(loc1+len(word)-1-len(line)-1)) 
                location.append(LOC.index(loc1)+1)
                location.append(abs(loc1+len(word)-1-len(line)-1)+len(word)-1)
                location.append(LOC.index(loc1)+1)
            #print (location)
    else:
        for loc in locations:
            if loc > 0:
                location.append(locations.index(loc)+1)
                location.append(loc)
                location.append(locations.index(loc)+1)
                location.append(loc+len(word)-1)
      
    return location

print (find_word("""xa
                 xb
                 x""", "ab"))
