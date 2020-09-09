maxd = 0
uni = []
a = input()
while a.find(' ') >= 0:
    *b, n = a.split(' ')
    x, y, z = tuple(map(float, b))
    for gal in uni:
        if maxd < (x - gal[0])**2 + (y - gal[1])**2 + (z - gal[2])**2:
            maxd = (x - gal[0])**2 + (y - gal[1])**2 + (z - gal[2])**2
            gal1 = n
            gal2 = gal[3]
    uni.append([x, y, z, n])
    a = input()
x = [gal1, gal2]
x.sort()
print(' '.join(x))