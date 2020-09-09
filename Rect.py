field = []
height = 0
rect_number = 0
line = input()
str = input()
while str != line:
    field += [list(str)]
    str = input()
    height += 1
width = len(str)
for i in range(height):
    for j in range(width):
        if field[i][j] == '#':
            rect_height = 1
            rect_width = 1
            rect_number += 1
            while (j + rect_width < width) and (field[i][j + rect_width] == '#'):
                rect_width += 1
            while (i + rect_height < height) and (field[i + rect_height][j] == '#'):
                rect_height += 1
            for k in range(i, i + rect_height):
                field[k][j:j + rect_width] = rect_width * "."
print(rect_number)