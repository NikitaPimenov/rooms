def shex(n):
    if not n:
        return ''
    return shex(n // 64) + chr((n % 64) + 32)


def xehs(s):
    x = 0
    for c in s:
        x = x * 64 + (ord(c) - 32)
    return x


def encode(txt):
    d = {}
    for i in txt:
        d[i] = 0
    for i in txt:
        d[i] += 1
    s = sorted(d.items(), key = lambda p: - 100 * p[1] - ord(p[0]))
    x = ''
    for i in range(len(s)):
        x += s[i][0]
    key = []
    for i in range(len(txt)):
        key.extend(list('1' * x.index(txt[i]) + '0'))
    key = ''.join(key)
    y = ''
    key += '0' * ((6 - len(key)) % 6)
    for i in range(len(key), 0, -6):
        y = chr(int(key[i - 6:i], 2) + 32) + y
    return len(txt), x, y


def decode(length, chars, code):
    key = ''
    for i in code:
        c = str(bin(ord(i) - 32))[2:]
        key += '0' * (6 - len(c)) + c
    txt = ''
    x = 0
    for i in key:
        if i != '0':
            x += 1
        else:
            txt += chars[x]
            x = 0
    return txt[:length]