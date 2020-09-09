def moar(a, b, n):
    a_n, b_n = 0, 0
    for e in a:
        if e % n == 0:
            a_n += 1
    for e in b:
        if e % n == 0:
            b_n += 1
    return a_n > b_n