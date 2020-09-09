from fractions import Fraction
class sausage:
    def __init__(self, inside = 'pork!', d = 1):
        self.d = Fraction(d)
        self.inside = inside
    def __sub__(self, other):
        if self.d > other.d:
            d = self.d - other.d
        else:
            d = Fraction(0)
        return sausage(self.inside, d)
    def __add__(self, other):
        return sausage(self.inside, other.d + self.d)
    def __truediv__(self, num):
        return sausage(self.inside, self.d / num)
    def __mul__(self, num):
        return sausage(self.inside, self.d * num)
    __rmul__ = __mul__
    def __str__(self):
        n = 12 // len(self.inside)
        leng = self.d.limit_denominator(max_denominator=1)
        if leng > self.d:
            leng -= 1
        ost = ((self.d - leng) * 12)
        if ost.limit_denominator(max_denominator=1) <= ost:
            ost = ost.limit_denominator(max_denominator=1).numerator
        else:
            ost = ost.limit_denominator(max_denominator=1).numerator - 1
        v = ('/' + '-' * 12 + '\\') * leng.numerator
        s = ('\\' + '-' * 12 + '/') * leng.numerator
        inside = ('|' + self.inside * n + self.inside[:(-len(self.inside) * n) % 12] + '|') * leng.numerator
        if ost > 0:
            v += '/' + '-' * ost + '|'
            s += '\\' + '-' * ost + '|'
            n = ost // len(self.inside)
            if n != 0:
                inside += '|' + self.inside * n + self.inside[:(-len(self.inside) * n) % ost] + '|'
            else:
                inside += '|' + self.inside[:ost] + '|'
        elif leng == 0:
            v = '/|'
            s = '\\|'
            inside = '||'
        res = v + '\n' + 3 * (inside + '\n') + s
        return res
    def __bool__(self):
        if (self.d * 12).denominator != 1:
            return True
        return False