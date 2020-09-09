from collections import defaultdict
a = input()
map = defaultdict(list)
while a.find(' ') >= 0:
    x, y = a.split()
    map[x].append(y)
    map[y].append(x)
    a = input()
b = input()
x = set(map[a])
old_set = set()
while x != old_set and b not in x:
    old_set = x.copy()
    for i in old_set:
        for elem in map[i]:
            x.add(elem)
if b in x:
    print("YES")
else:
    print("NO")