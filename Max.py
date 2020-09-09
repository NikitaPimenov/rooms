x = int(input())
max_sum = x
sum = x
while x != 0:
    x = int(input())
    if x > 0:
        if sum < 0:
            sum = 0
        sum += x
    else:
        if sum > max_sum:
            max_sum = sum
        if sum + x > 0:
            sum += x
        else:
            sum = x
print(max_sum)