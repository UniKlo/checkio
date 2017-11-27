def long_repeat(line):
    import itertools
    c =[''.join(value) for key, value in itertools.groupby(line)]
    return len(max(c, key=len))
  

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
