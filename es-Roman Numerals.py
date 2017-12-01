def checkio(data):
    u=""
    d=""
    c=""
    m=""
    
    lst = [int(x) for x in str(data)]
    lst = lst[::-1]
    if 0<lst[0]<=3:
        u=lst[0]*'I'
    elif lst[0]==4:
        u="IV"
    elif lst[0]==5:
        u="V"
    elif 5<lst[0]<=8:
        u="V"+(lst[0]-5)*'I'
    elif lst[0]==9:
        u="IX"
        
    try:
        if lst[1]==1 and lst[0]==0:
            d="X"
        elif 0<lst[1]<=3:
            d=lst[1]*'X'
        elif lst[1]==4:
            d="XL"
        elif lst[1]==5:
            d="L"
        elif 5<lst[1]<=8:
            d="L"+(lst[1]-5)*'X'
        elif lst[1]==9:
            d="XC"  
    except:
        pass

    try:
        if lst[2]==1 and lst[1]==0 and lst[0]==0:
            c="C"
        elif 0<lst[2]<=3:
            c=lst[2]*'C'
        elif lst[2]==4:
            c="CD"
        elif lst[2]==5:
            c="D"
        elif 5<lst[2]<=8:
            c="D"+(lst[2]-5)*'C'
        elif lst[2]==9:
            c="CM"  
    except:
        pass
     
    try:
        if lst[3]==1 and lst[2]==0 and lst[1]==0 and lst[0]==0:
            m="M"
        elif 0<lst[3]<=3:
            m=lst[3]*'M' 
    except:
        pass
    
    return m+c+d+u
            
