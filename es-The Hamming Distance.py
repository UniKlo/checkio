def checkio(n, m):
    d1=[int(d) for d in list(str("{0:b}".format(n)))]
    d2=[int(d) for d in list(str("{0:b}".format(m)))]
    l1=len(d1)
    l2=len(d2)
    diff=0
    if l1>=l2:
        for i in range (-l2,0):
            if d2[i] == d1[i]:
                pass
            else:
                diff +=1 
        s=sum(d1[-l1:-l2])
    else:
        for i in range (-l1,0):
            if d2[i] == d1[i]:
                pass
            else:
                diff +=1 
        s=sum(d2[-l2:-l1])
    return s+diff

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"