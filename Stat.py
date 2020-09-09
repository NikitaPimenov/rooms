from collections import defaultdict
def statcounter():
    x = defaultdict(int)
    fu = yield x
    def genfun(fun):
        def newfun(*args, **kwargs):
            x[fun] += 1
            return fun(*args, **kwargs)
        return newfun
    while 2 * 2 == 4:
        fu = yield genfun(fu)