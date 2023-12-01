#Smallest Multiple
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Mathematically what we need to do is find the list of all prime factors occuring between 1-20 and their highest frequency.

#I note that finding the smallest positive integer evenly divisibly by 1 through n is much easier than m through n.
# This is because 1-n can be done by looking at all primes and powers of primes occuring in 1-n and simply multiplying
#  the highest power occurence of each prime together.

import numpy as np

def primesUpTo(n):
    primes = []
    potentialPrimes = list(range(2,n+1))
    while len(potentialPrimes) > 0 :
        p = potentialPrimes.pop(0)
        primes.append(p)
        potentialPrimes = [x for x in potentialPrimes if (x % p != 0)]
    return primes

def greatestPowerLessEqual(p,n):
    i = 0
    while p**(i+1) <= n:
        i+=1
    return p**i

def primePowersUnder(n):
    primes = primesUpTo(n)
    return list(map(lambda p : greatestPowerLessEqual(p,n), primes))

print("What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?")
print("Answer: {}".format(np.prod(primePowersUnder(20))))    