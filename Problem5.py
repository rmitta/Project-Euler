#Smallest Multiple
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Mathematically what we need to do is find the list of all prime factors occuring between 1-20 and their highest frequency.

#I note that finding the smallest positive integer evenly divisibly by 1 through n is much easier than m through n.
# This is because 1-n can be done by looking at all primes and powers of primes occuring in 1-n and simply multiplying
#  the highest power occurence of each prime together.

import numpy as np

def primesUpTo(n):
    primesList = []
    primes = np.ones(n+1, dtype=np.bool_)
    for p in range(2,n+1):
        if primes[p]:
            primesList.append(p)
            for m in range(p,n+1,p):
                primes[m] = False
    return primesList

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