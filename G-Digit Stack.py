def golf(commands):
    stack=[]
    total=0
    for command in commands:
        command=command.split()
        if 'PUSH' in command:
            stack.append(int(command[1]))
        elif 'POP' in command:
            try:
                a=stack.pop()
                total += a
            except:
                pass
        else:
            try:
                total+= stack[-1]
            except:
                pass
    return total


            


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf(("PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK")) == 8, "Example"
    assert golf(("POP", "POP")) == 0, "PopPop"
    assert golf(("PUSH 9", "PUSH 9", "POP")) == 9, "Push 9"
    assert golf(()) == 0, "Empty"
    print("All done? Earn rewards by using the 'Check' button!")
