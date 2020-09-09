a = input()
b = input()
shift = 0
pos = 0
flag = True
end = 0
while not (end == len(b) and not flag or pos == -1):
    if flag:
        start = 0
        end = b.find('@')
        if end == -1:
            end = len(b)
        pos = a.find(b[start:end], shift)
        flag = False
    else:
        start = end + 1
        end = b.find('@', start)
        if end == -1:
            end = len(b)
        flag = a[pos + start:].find(b[start:end]) != 0
        if flag:
            shift = pos + 1
print(pos)