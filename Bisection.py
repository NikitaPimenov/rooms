from math import *

def func(x, string ):
    return eval(string )
string = input()
a, b = eval(input())
while abs(func((a + b) / 2, string )) > 0.000001:
    if func(a, string ) * func((a + b) / 2, string ) < 0:
        b = (a + b) / 2
    else:
        a = (a + b) / 2
print((a + b) / 2)