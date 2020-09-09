class morse:
    di = 'di'
    dit = 'dit'
    dah = 'dah'
    space = ' '
    gap = ','
    end = '.'

    def __init__(self, s=''):
        self.zero = 1
        self.code = ''
        if s != '':
            l = s.split()
            if len(l) != 1:
                self.di = l[0]
                if len(l) == 2:
                    self.dit = l[0]
                    self.dah = l[1]
                else:
                    self.dit = l[1]
                    self.dah = l[2]
                    if len(l) == 4:
                        self.end = l[3]
                    if s[-1] == ' ':
                        self.end = ''
            else:
                self.di = l[0][0]
                self.space = ''
                self.gap = ' '
                self.end = ''
                if len(l[0]) != 2:
                    self.dit = l[0][1]
                    self.dah = l[0][2]
                    self.end = l[0][3:]
                else:
                    self.dit = l[0][0]
                    self.dah = l[0][1]

    def __pos__(self):
        if self.zero:
            self.code = self.dit
            self.zero = 0
        elif self.code[0] == self.gap:
            self.code = self.dit + self.code
        else:
            self.code = self.di + self.space + self.code
        return self

    def __neg__(self):
        if self.zero or self.code[0] == self.gap:
            self.zero = 0
            self.code = self.dah + self.code
        else:
            self.code = self.dah + self.space + self.code
        return self

    def __invert__(self):
        self.code = self.gap + self.space + self.code
        return self

    def __str__(self):
        return self.code + self.end