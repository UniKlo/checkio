def count_ingots(report):
    
    alphabet = []
    for letter in range(65,91):
        alphabet.append(chr(letter))    
    
    inventory=[]
    for char in alphabet:
        for number in range (1,10):
            inventory.append(char+str(number))
    #print (inventory)
    
    report=report.split(",")
    sum=0
    for location in report:
        sum=sum+inventory.index(location)+1
    return sum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_ingots("A2,B1") == 12, "Two and ten"
    assert count_ingots("A1,A1,A1") == 3, "One, two, three"
    assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
    assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
