#Distinct Primes Factors

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import math
from Utils.Primes import Primes



def primeFactorisation(n : int, primesObject : Primes):
    """Calculate the prime factorisation of a number n, assuming primesObject contains a list of primes up to sqrt(n)

    Args:
        n (int): The number to factorise
        primesObject (Primes): A Primes object containing at least primes up to sqrt(n)

    Raises:
        Exception: If we do not have access to primes up to sqrt(n)

    Returns:
        factors (list[int]): The list of prime factors of n, in order, with duplicates
    """
    sqrtn = math.isqrt(n)
    if primesObject.checked < sqrtn:
        raise Exception(f"Must have checked primes upto sqrt {n}, i.e. {sqrtn}")
    
    factors : list[int] = []
    primeIndex = 0
    while n > 1:
        p = primesObject.list[primeIndex]
        if p > sqrtn: #Then the remaining n must be prime
            factors.append(n)
            n = 1
        
        while n % p == 0:
            factors.append(p)
            n = n // p
        primeIndex += 1
        
    return factors

def main(m_consecutive = 4, distinct_factors = 4):
    primes = Primes()
    primes.upto(10000)
    
    found = False
    consecutives = []
    n = 1
    
    while not found:
        n += 1
        factors = primeFactorisation(n, primes)
        if len(set(factors)) >= distinct_factors:
            consecutives.append(n)
            if len(consecutives) >= m_consecutive:
                found = True
        else:
            consecutives = []
    
    return consecutives[0]
        
if __name__ == "__main__":
    main()