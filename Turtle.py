def turtle(coord, direction):
    if direction == 0:
	    x, y = 1, 0
    elif direction == 1:
	    x, y = 0, 1
    elif direction == 2:
	    x, y = -1, 0
    elif direction == 3:
	    x, y = 0, -1
    a = yield coord
    while True:
        if a == 'f':
            coord = coord[0] + x, coord[1] + y
        elif a == 'l':
            x0, y0 = x, y
            if x0 + y0 == 1:
                x -= 1
            else:
                x += 1
            if x0 - y0 == -1:
                y -= 1
            else:
                y += 1
        elif a == 'r':
            x0, y0 = x, y
            if x0 - y0 == -1:
                x += 1
            else:
                x -= 1
            if x0 + y0 == 1:
                y -= 1
            else:
                y += 1
        a = yield coord