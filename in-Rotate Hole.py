import numpy as np
def rotate(state, pipe_numbers):
    print ('len of the state: ',len(state))
    state=np.array(state)
    answer=[]
    turns=0
    while turns < (len(state)-1):
        '''
        for position in range (len(state)):
            print ('position: ', position)
            for n in pipe_numbers:
                #print ('state[n]: ', state[n])
                if state[n]!=1:
                    answer=[]
                    break
                else:
                    answer.append(position)
            answer.append(position)
            '''
        turns +=1
        print (turns)
        print (np.roll(state,turns))
        #print (state)
    return answer


print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
'''