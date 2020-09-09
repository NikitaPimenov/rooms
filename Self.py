class WeAre:
    ___x = 0
    @classmethod
    def __init__(self):
        self.___x += 1
    @property
    def count(self):
        return self.___x
    @count.setter
    def count(self, v):
        pass
    @count.deleter
    def count(self):
        pass
    @classmethod
    def __del__(self):
        self.___x -= 1