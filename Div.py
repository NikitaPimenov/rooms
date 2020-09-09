class DivStr(str):
    def __truediv__(self, div):
        return self[:len(self) // div]
    ne_nado = ('__class__', '__new__', '__getattribute__', '__getattr__', '__repr__', '__str__')
    for obj in str.__dict__:
        if obj not in ne_nado and callable(str.__dict__[obj]):
            e = f'''def {obj}(self, *a):
            x = str.__dict__["{obj}"](self, *a)
            if type(x) == str:
                x = DivStr(x)
            return x'''
            exec(e)
