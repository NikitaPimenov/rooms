class Kostyl:
    pass
class LetterAttr(Kostyl):
    def __getattr__(self, v):
        self.__setattr__(v, v)
        return v
    def __setattr__(self, k, x):
        y = ''
        if k not in dir(self):
            old = k
        else:
            old = self.__getattribute__(k)
        for c in x:
            if c in old:
                y += c
        x = y
        Kostyl.__setattr__(self, k, x)
