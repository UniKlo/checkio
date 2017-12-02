def checkio(first, second):
    F=first.split(",")
    S=second.split(",")
    clst=[]
    for f in F:
        if f in S:
            clst.append(f)

    clst.sort(key=str.lower)
    return ','.join(clst)


if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
