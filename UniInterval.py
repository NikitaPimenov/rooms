tup = list(eval(input()))
tup.sort()
x_0, y_0 = tup[0]
uni = y_0 - x_0
for x, y in tup:
    if y_0 < x:
        x_0 = x
        y_0 = y
        uni += y_0 - x_0
    elif y_0 < y:
        uni += y - y_0
        y_0 = y
print(uni)