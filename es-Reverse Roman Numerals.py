ROMANS = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

def reverse_roman(roman_string):
    lst=list(roman_string)
    s=0
    for i in range(0,len(lst)):
        if (i+1)<len(lst) and ROMANS[lst[i]] < ROMANS[lst[i+1]] :
            s=s-(ROMANS[lst[i]])
        else: 
            s=s+(ROMANS[lst[i]])      
    return s



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');