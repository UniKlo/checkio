def simple_areas(*args):
    from numpy import prod
    if len (args)>2:
        a,b,c = args
        p=sum(args)/2
        area=(p*(p-a)*(p-b)*(p-c))**(1/2)
    elif len(args)<2:
        from math import pi
        a,=args     
        area=0
        area=round(pi/4*a**(2),2)
    else:
        area= prod(args)
    return area

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    print("Earn cool rewards by using the 'Check' button!")
