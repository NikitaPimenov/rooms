def BinPow(a, n, f):
    if n % 2 == 1 and n > 1:
        return f(BinPow(a, n-1, f), a)
    if n % 2 == 0:
        return f(BinPow(a, n//2, f), BinPow(a, n//2, f))
    return a