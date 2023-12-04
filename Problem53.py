#Combinatoric Selections
#How many, not necessarily distinct, values of n choose r for 1 <= n <= 100, are greater than one-million?


#Notes: if n choose r > 1m, and m > n, then m choose r > 1m 
#Therefore our method is as such: for each r, go through n's until we find one that yields a value > 1m. 


import math

def nsYieldingGreater(r):
    for n in range(r,101):
        if math.comb(n,r) >= 1000000:
            return 101 - n
    return 0

ans = 0
for r in range(1,101):
    ans += nsYieldingGreater(r)

print(ans)