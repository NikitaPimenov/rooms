queue = []
str = eval(input())
if type(str) != int:
    tup = tuple(str)
    for i in tup:
        if type(i) == tuple:
            queue += [k for k in i]
        if type(i) == int:
            if i > len(queue):
                break
            else:
                print(tuple(queue[0:i]))
                for k in range(i):
                    queue.remove(queue[0])