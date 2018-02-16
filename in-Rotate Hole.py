import numpy as np
np.set_printoptions(threshold=np.nan)
def rotate(state, pipe_numbers):
    #print ('len of the state: ',len(state))
    state=np.array(state)
    answer=[]
    turns=0
    while turns < (len(state)):

        test=[]
        for n in pipe_numbers:
            #print ('state[n]: ', state[n])
            test.append(state[n])
        #print ('test: ',test)
        if 0 in test:
            pass
        else:
            answer.append(turns)
            
        state=np.roll(state,1)
        turns +=1
        
    return answer

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"

