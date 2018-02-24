def convert(numerator, denominator):
    #print("---->", numerator, "/", denominator)
    result = [str(numerator//denominator) + "."]
    subresults = [numerator % denominator]          ### changed ###
    numerator %= denominator
    while numerator != 0:
        #print(numerator)
        numerator *= 10
        result_digit, numerator = divmod(numerator, denominator)
        result.append(str(result_digit))             ### moved before if-statement

        if numerator not in subresults:
            subresults.append(numerator)
            #print("appended", result_digit)

        else:
            result.insert(subresults.index(numerator) + 1, "(")   ### added '+ 1'
            #print("index", subresults.index(numerator), subresults, "result", result)
            result.append(")")
            #print("repeating", numerator)
            break
    #print(result)
    return "".join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"

    print("Earn cool rewards by using the 'Check' button!")
