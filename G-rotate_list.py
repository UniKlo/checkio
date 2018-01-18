# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:42:21 2018

@author: khloe
"""

def rotate_list(elements, rotates):
    newl=[]
    for i in range (0,len(elements)):
       print (elements[i])
       
    return elements

print (rotate_list([1, 2, 3, 4, 5, 6], 2))
'''
if __name__ == '__main__':
    assert rotate_list([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2], "First"
    assert rotate_list([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3], "Second"
    assert rotate_list([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6], "Third"

    print("All set? Click \"Check\" to review your code and earn rewards!")
'''
