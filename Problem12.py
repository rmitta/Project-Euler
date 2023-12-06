#Highly Divisible Triangular Number
#What is the value of the first triangle number to have over five hundred divisors?
import math
class triangularNumbers:
    def __init__(self) -> None:
        self.num = (1,1)
    
    def next(self):
        (x,y) = self.num
        self.num = (x+1,y+x+1)
    
    def divisors(self) -> int:
        #Extend primesList up to self.num
        #Calculate divisors
        return divisors

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
            if p < sqrtn:
                potentialPrimes = [x for x in potentialPrimes if (x % p != 0)]

