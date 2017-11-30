def checkio(words):
    c=[]
    import re
    d = re.split('(\d+)',words)

    
    for i in d:
        sublist=i.strip().split()
        if len(sublist)>2:
            c.append(len(sublist))
    if len(c)>0:
        return True
    else:
        return False

print (checkio("He is 123 man"))
print (checkio("one two 3 four five six 7 eight 9 ten eleven 12"))