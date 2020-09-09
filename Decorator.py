def nonify(fun):
    def newfun(*args, **kwargs):
        x = fun(*args, **kwargs)
        if not x:
            return None
        return x
    return newfun