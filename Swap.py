shift = 0
dec = 0
answer = 0
k = int(input())
prev = k
next = k
if k > 1:
    while ((next != 1) or (prev != 0)):
        prev = next
        next = (prev * k + shift) % 10
        shift = (prev * k + shift) // 10
        answer += next * (10 ** dec)
        dec += 1
    answer = answer * 10 + k
    print(answer)
else:
    if k == 0:
        print(0)
    else:
        print(1)