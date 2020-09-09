c = -1
star = ()
k = 0


def randint(a, b):
    global c
    c *= -1
    if c == 1:
        return a
    else:
        return b


def randrange(a, b='', d=1, p='Hello, world!'):
    global star
    global k
    if (a, b, d) != star:
        k = 0
        star = (a, b, d)
    if b is '':
        b,a = a, 0
    x = a + k
    k = (k + d) % (b - a)
    return x