htonum={1:5,13:5,2:10,14:10,3:15,15:15,4:20,16:20,5:25,17:25,6:30,18:30,7:35,19:35,8:40,20:40,9:45,21:45,10:50,22:50,11:55,23:55,12:0,24:0,00:0}
def clock_angle(time):
    try:
        minnum = int(time[3:])
    except:
        minnum = 0
    try:
        sideh= int(time [:2])
    except:
        sideh=0
    for hour,num in htonum.items():
        if sideh == hour:
            diff= abs((num)+(minnum/60)*5-minnum)
            if diff>30:
                return round(6*(60-diff),1)
            elif diff==0:
                return 0
            else:
                return round(6*diff,1)





if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
