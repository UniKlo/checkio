def letter_queue(commands):
    stack=[]

    for command in commands:
        command=command.split()
        if 'PUSH' in command:
            stack.append((command[1]))
        elif 'POP' in command:
            try:
                del stack[0]
            except:
                pass

    return "".join(stack)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT", "dot example"
    assert letter_queue(("POP", "POP")) == "", "Pop, Pop, empty"
    assert letter_queue(("PUSH H", "PUSH I")) == "HI", "Hi!"
    assert letter_queue(()) == "", "Nothing"

    print("All done? Earn rewards by using the 'Check' button!")
