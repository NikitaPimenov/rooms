def sizer(cls):
    class dsc:
        def __get__(self, x, c):
            if '__len__' not in dir(x):
                return int(x)
            return len(x)
    class res(cls):
        size = dsc()
    return res