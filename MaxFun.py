def maxfun(s, f1, *f):
    sum1 = 0
    max = f1
    for x in s:
        sum1 += f1(x)
    for i, func in enumerate(f):
        sum = 0
        for x in s:
            sum += func(x)
        if sum >= sum1:
            max = func
            sum1 = sum
    return max