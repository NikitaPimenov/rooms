N, M = eval(input())
print("=" * M)
shift_0 = 0
shift_1 = 0
x = N
while x != 0:
    x = x // 10
    shift_0 += 1
x = N*N
while x != 0:
    x = x // 10
    shift_1 += 1
columns = (M + 3) // (2 * shift_0 + shift_1 + 9)
lines = (N - 1) // columns + 1
for line in range(lines):
    for b in range(1, N + 1):
        x = line * columns + 1
        print(f"{x:{shift_0}} * {b:<{shift_0}} = {x * b:<{shift_1}}", end='')
        for column in range(1, columns):
            a = column + x
            if a > N:
                break
            print(f" | {a:={shift_0}} * {b:<{shift_0}} = {a * b:<{shift_1}}", end='')
        print()
    print("=" * M)