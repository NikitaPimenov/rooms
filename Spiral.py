M, N = eval(input())
table = [[0 for j in range(M)] for i in range(N)]
M -= 1
N -= 1
digits = 0
for shift in range(0, (min(M, N) + 1) // 2):
    for right in range(shift, M - shift):
        table[shift][right] = digits
        digits = (digits + 1) % 10
    for down in range(shift, N - shift):
        table[down][M - shift] = digits
        digits = (digits + 1) % 10
    for left in range(shift, M - shift):
        table[N - shift][M - left] = digits
        digits = (digits + 1) % 10
    for up in range(shift, N - shift):
        table[N - up][shift] = digits
        digits = (digits + 1) % 10
shift = (min(M, N) + 1) // 2
if (N <= M) and (N % 2 == 0):
    for right in range(shift, M - shift + 1):
        table[shift][right] = digits
        digits = (digits + 1) % 10
if (M < N) and (M % 2 == 0):
    for down in range(shift, N - shift + 1):
        table[down][M - shift] = digits
        digits = (digits + 1) % 10
for i in range(N + 1):
    for j in range(M):
        print(table[i][j], end=' ')
    print(table[i][M])