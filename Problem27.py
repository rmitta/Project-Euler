#Quadratic Primes

#See project euler for question description.

from Utils.Primes import Primes

primes = Primes()
primes.upto(4000000)
primeSet = set(primes.list)

def quadratic(n,a,b):
    return n**2 + a*n + b

best = (0,0,0)

for a in range(-999,1000):
    for b in range(-999,1001, 2):  #step 2 because we can immediately discount even b's
        n = 0
        while quadratic(n,a,b) in primeSet:
            n += 1
        n -= 1
        if n > best[0]:
            best = (n,a,b)

print(best)
print(best[1] * best[2])