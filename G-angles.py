def angles(a, b, c):
    from math import acos, degrees
    lst=[]
    try:
        lst.append(round(degrees(acos((a*a + b*b - c*c)/(2.0*a*b)))))
        lst.append(round(degrees(acos((a*a + c*c - b*b)/(2.0*a*c)))))
        lst.append(round(degrees(acos((c*c + b*b - a*a)/(2.0*c*b)))))
        
        if sum(lst) == 180 and lst.count(0)==0:      
            return sorted(lst)
        else:
            return [0, 0, 0]
    except:
        return [0, 0, 0]
   

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
