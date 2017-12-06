def checkio(data):
    data1='+'.join(map(str, data))  
    s=data1
    return eval(s)

print ( checkio([1,2,3]))