def pigen():
    i = 1
    k = -1
    pi = 1
    while 2 + 2 == 4:
        yield 4 * pi
        pi += k / (2 * i + 1)
        i += 1
        k = k * (-1)