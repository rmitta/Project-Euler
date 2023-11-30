#Largest Prime Factor
#What is the largest prime factor of the number 600851475143?

#My first idea is to use the an Eratosthenes seive style method to find (all) prime factors.
#I think that is computationally more or less required to find the largest prime factor.

import math

n = 600851475143

def primeFactorisation(n):
    primeFactorisation = []
    potentialDivisors = list(range(2,math.isqrt(n)))

    while len(potentialDivisors) > 0 :
        p = potentialDivisors.pop(0)

        while n % p == 0:
            n //= p
            primeFactorisation.append(p)
            sqrtn = math.isqrt(n)
            potentialDivisors = [x for x in potentialDivisors if (x % p != 0) and (x <= sqrtn) ]
        
    if n != 1:
        primeFactorisation.append(n)

    return primeFactorisation

print(primeFactorisation(600851475143))