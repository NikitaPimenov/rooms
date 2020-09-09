def fcounter(C, *args):
    a, b, c, d = [], [], [], []
    for e in dir(C):
        if (e + '_').index('_') != 0:
            if not callable(getattr(C, e)):
                b.append(e)
            else:
                a.append(e)
    A = C(*args)
    for e in dir(A):
        if (e + '_').index('_') != 0:
            if callable(getattr(A, e)):
                if e not in a:
                    c.append(e)
            else:
                if e not in b:
                    d.append(e)
    return sorted(a), sorted(b), sorted(c), sorted(d)