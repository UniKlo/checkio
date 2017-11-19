# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:46:56 2017

@author: khloe
"""

def find_message(text):
    import re
    newtext= re.findall('[A-Z]',text)
    return ''.join(newtext)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
