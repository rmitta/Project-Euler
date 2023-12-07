#Highly Divisible Triangular Number
#What is the value of the first triangle number to have over five hundred divisors?
import math
import numpy as np

class primesList:
    def __init__(self) -> None:
        self.UpTo = 2
        self.list = [2]
    
    def extend(self,n) -> None:
        potentialPrimes = list(range(self.UpTo + 1, n+1))
        for p in self.list:
            potentialPrimes = [x for x in potentialPrimes if (x % p != 0)]
        sqrtn = math.isqrt(n)
        while len(potentialPrimes) > 0:
            p = potentialPrimes.pop(0)
            self.list.append(p)
            if p <= sqrtn:
                potentialPrimes = [x for x in potentialPrimes if (x % p != 0)]
        self.UpTo = max(self.UpTo, n)

class triangularNumbers:
    def __init__(self) -> None:
        self.num = (1,1)
        self.primes = primesList()
    
    def next(self):
        (x,y) = self.num
        self.num = (x+1,y+x+1)
    
    def primePowerDivisors(self) -> int:
        (_,x) = self.num
        #Extend primesList to sqrt(num) (this was key, extending to num was far too slow)
        sqrt = math.isqrt(x)
        if sqrt >= self.primes.UpTo:
            self.primes.extend(sqrt)
        #Calculate prime divisors
        primeDivs = [p for p in self.primes.list if x % p == 0]
        powersDividing = []
        for p in primeDivs:
            i = 0
            while x % p == 0:
                i += 1
                x = x // p
            powersDividing.append(i)
        return (primeDivs,powersDividing)
        
    def numDivisors(self) -> int:
        (_,powersDividing) = self.primePowerDivisors()
        return np.product([i+1 for i in powersDividing])

def soln() -> (int,int):
    tri = triangularNumbers()
    while tri.numDivisors() <= 500:
        tri.next()
        print(tri.num, tri.numDivisors())
    return tri.numDivisors(),tri.num

print(soln())


