import math

a = int(input())
i = 2
bool = True
while (bool and (i <= (math.sqrt(a) + 1))):
    temp = a
    if temp != i:
        while ((temp % i == 0) and (temp != 1)):
            temp = temp // i
        if temp == 1:
            bool = False
    i += 1
if bool:
    print('NO')
else:
    print('YES')