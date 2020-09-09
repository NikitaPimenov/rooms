def fix(n):
    def debug(fun):
        def newfun(*args, **kwargs):
            a = []
            for x in args:
                if type(x) == float:
                    a += [round(x, n)]
                else:
                    a += [x]
            b = dict.fromkeys(kwargs.keys())
            for x, y in kwargs.items():
                if type(y) == float:
                    b[x] = round(y, n)
                else:
                    b[x] = y
            ans = fun(*a, **b)
            if type(ans) == float:
                return round(ans, n)
            return ans
        return newfun
    return debug