def swap_sort(array):
    lst=list(array)
    move=''
    newlst=sorted(lst)

    for i in range (len(lst)):
        while lst[i]!= newlst[i]:
            for n in range (len(lst)-1):
                while lst[n]> lst[n+1]:
                    lst[n],lst[n+1]= lst[n+1],lst[n]
                    if move == '':
                        move=str(n)+str(n+1)
                    else:
                        move=move+','+str(n)+str(n+1)
                      
    return move


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(f, indata):
        result = f(indata)
        array = list(indata[:])
        la = len(array)
        if not isinstance(result, str):
            print("The result should be a string")
            return False
        actions = result.split(",") if result else []
        for act in actions:
            if len(act) != 2 or not act.isdigit():
                print("The wrong action: {}".format(act))
                return False
            i, j = int(act[0]), int(act[1])
            if i >= la or j >= la:
                print("Index error: {}".format(act))
                return False
            if abs(i - j) != 1:
                print("The wrong action: {}".format(act))
                return False
            array[i], array[j] = array[j], array[i]
        if len(actions) > (la * (la - 1)) // 2:
            print("Too many actions. BOOM!")
            return False
        if array != sorted(indata):
            print("The array is not sorted. BOOM!")
            return False
        return True

    assert check_solution(swap_sort, (6, 4, 2)), "Reverse simple"
    assert check_solution(swap_sort, (1, 2, 3, 4, 5)), "All right!"
    assert check_solution(swap_sort, (1, 2, 3, 5, 3)), "One move"

    print("Earn cool rewards by using the 'Check' button!")
