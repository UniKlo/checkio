def count_words(text, words):
    import re
    text = text.lower()
    
    newtext=text
    for word in words:
        newtext = re.sub(word, "1", newtext)
    count = newtext.count('1')
    if count > len(words):
        count=len(words)
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
