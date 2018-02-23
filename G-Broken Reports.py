import re


def golf(broken_report):
    
    report=re.findall('[A-Z][1-9]',broken_report)
    inventory=[]
    for letter in range(65,91):
        for number in range (1,10):
            inventory.append(chr(letter)+str(number))

    sum=0
    for location in report:
        sum=sum+inventory.index(location)+1
    return sum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf("ASDA1,BB22D01C1") == 31
    assert golf("B1,C2,D3") == 60
    print("Earn cool rewards by using the 'Check' button!")
    
