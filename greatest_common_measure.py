def greatest_common_measure(pair):
    a,b = pair
    low = min(a,b)
    for i in range(low,0,-1):
        if a%i==0 and b%i==0:
            return i
    assert False, "Niedostepny"


