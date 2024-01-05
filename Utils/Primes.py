import math
import numpy as np

def _removeMultiplesOf(prime : int, lst : list[int]):
    """Removes all occurences of multiples of p from lst"""
    return [x for x in lst if (x % prime != 0)]

class Primes():
    """Stores lists of primes."""
    def __init__(self) -> None:
        self.list = []
        self.checked = 1

#    @profile
    def extend(self, n, chunkSize = 100000):
        """Extend the primeslist by n new primes. Searches chunks of chunkSize integers at a time."""
        potentialPrimes = []
        prevLen = len(self.list)
        while len(self.list) < prevLen + n:
            #When necessary extend the range of our search
            if not potentialPrimes:
                potentialPrimes = list(range(self.checked + chunkSize,self.checked,-1))
                self.checked += chunkSize
                #Remove multiples of already checked primes (less than sqrt max to check)
                sqrtMaxToCheck = math.sqrt(self.checked)
                for p in self.list:
                    if p <= sqrtMaxToCheck:
                        potentialPrimes = _removeMultiplesOf(p,potentialPrimes)

            #Main step: take next prime, add it to list, remove multiples.
            p = potentialPrimes.pop()
            self.list.append(p)
            if p <= sqrtMaxToCheck:
                potentialPrimes = _removeMultiplesOf(p,potentialPrimes)
            
        self.checked = self.list[-1] #Because the while loop cuts off halfway through a chunk.
    
#    @profile
    def upto(self, n):
        """Initialize primeslist to be all primes upto n"""
        potentialPrimes = np.ones(n+1,dtype = np.bool_)
        potentialPrimes[0:2] = np.False_
        for i in range(2,math.isqrt(n)+1):
            if potentialPrimes[i]:
                potentialPrimes[np.arange(i*2,n+1,i)] = np.False_
        
        self.list = np.nonzero(potentialPrimes)[0]
        self.checked = n