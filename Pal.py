reverse = 0
num = int(input())
a = num
while a > 0:
    reverse = reverse * 10 + a % 10
    a = a // 10
if reverse == num:
    print('YES')
else:
    print('NO')