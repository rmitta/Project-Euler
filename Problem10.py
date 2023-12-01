#Summation of Primes
#Find the sum of all the primes below two million.

#We already wrote code for finding primes below a number in Problem5:
#It was too slow, so we sped it up by adding the condition that we don't need to check for multiples of primes above sqrt(2mil)
import math

def primesUpTo(n):
    primes = []
    potentialPrimes = list(range(2,n+1))
    sqrtn = math.isqrt(n)
    while len(potentialPrimes) > 0 :
        p = potentialPrimes.pop(0)
        primes.append(p)
        if p < sqrtn:
            potentialPrimes = [x for x in potentialPrimes if (x % p != 0)]
    return primes

def sumPrimesBelow(n):
    return sum(primesUpTo(n-1))

print(sumPrimesBelow(2000000))