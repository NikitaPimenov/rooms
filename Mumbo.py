flag = 0
alph = [{' '}, {' '}]
str = input()
while str != '':
    for s in str:
        alph[flag] = alph[flag] | {s}
    flag = (flag + 1) % 2
    str = input()
if len(alph[0]) > len(alph[1]):
    print("Mumbo")
else:
    print("Jumbo")