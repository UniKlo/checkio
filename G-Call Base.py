import math

def total_cost(calls):
    summary={}
    sumtime=[]
    for record in calls:
        if record[5:10] not in summary:
            summary[record[5:10]]=[math.ceil(int(record[20:])/60)]
        else:
            summary[record[5:10]].append(math.ceil(int(record[20:])/60))
    
    for key,value in summary.items():
        sumtime.append(sum(value))

    cost=0

    for item in sumtime:
        if item <= 100:
            cost=cost+item*1
        else:
            cost=cost+100+(item-100)*2
    return cost



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"

    print("All set? Click 'Check' to review your code and earn rewards!")
