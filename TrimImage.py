*t, s = input().split(' ')
x, y, length, width = tuple(map(int, t))
right = left = x
down = up = y
z = []
while (x, y, length, width) != (0, 0, 0, 0):
    if length != 0 and width != 0:
        if length > 0:
            x_0, x_1 = (x, x + length)
        else:
            x_0, x_1 = (x + length, x)
        if width > 0:
            y_0, y_1 = (y, y + width)
        else:
            y_0, y_1 = (y + width, y)
        z.append((x_0, y_0, x_1, y_1, s))
        right = max(right, x_1)
        down = max(down, y_1)
        left = min(left, x_0)
        up = min(up, y_0)
    *t, s = input().split(' ')
    x, y, length, width = tuple(map(int, t))
area = [list('.') * (right - left) for i in range(down - up)]
for x0, y0, x1, y1, ch in z:
    for i in range(x0 - left, x1 - left):
        for j in range(y0 - up, y1 - up):
            area[j][i] = ch
a = list(map(''.join, area))
print('\n'.join(a))