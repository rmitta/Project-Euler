#Prime Digit Replacements
#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

#
from itertools import combinations
from line_profiler import LineProfiler
import numpy as np

def replaceDigits(num,digit,positions):
    numStr = str(num)
    for position in positions:
        numStr = numStr[:position] + digit + numStr[1+position:]
    return int(numStr)

def digitReplaceFamily(num,positions):
    return [replaceDigits(num,str(digit),positions) for digit in range(10)]

def enumeratePositionOptions(numLength):
    onlyMultiplesOf3 = True
    if onlyMultiplesOf3:
        numChangeRange = range(3,numLength+1,3)
    else:
        numChangeRange = range(1,numLength+1)
    changes = []
    for numChanges in numChangeRange:
        changes += list(combinations(range(numLength),numChanges))
    return changes

def primesBitArray(primesList,maxN):
    bitArray = np.zeros((maxN+1), dtype=np.bool_)
    for p in primesList:
        bitArray[p] = True
    return bitArray

def checkPrimesList(primesList,maxN):
    bitArray = primesBitArray(primesList,maxN)
    for prime in primesList:
        for positions in enumeratePositionOptions(len(str(prime))):
            family = digitReplaceFamily(prime,positions)        #This takes all the time now.
            if len([x for x in family if bitArray[x]]) == 8:
                if len(str(family[0])) == len(str(prime)):
                    return family
    return "No 8 prime family found in primesList"

import math
def primesUpTo(n):
    primes = []
    potentialPrimes = list(range(2,n+1))
    sqrtn = math.isqrt(n)
    while len(potentialPrimes) > 0 :
        p = potentialPrimes.pop(0)
        primes.append(p)
        if p <= sqrtn:
            potentialPrimes = [x for x in potentialPrimes if (x % p != 0)]
    return primes


#checkPrimesList(primesUpTo(100000))

lp = LineProfiler()
lp.add_function(replaceDigits)
lp_wrapper = lp(checkPrimesList)
lp_wrapper(primesUpTo(10000000),10000000)
lp.print_stats()

#This family [2090021, 2191121, 2292221, 2393321, 2494421, 2595521, 2696621, 2797721, 2898821, 2999921] works but isn't the smallest I guess? Unless my primes list is wrong

#Just realised we can reduce our search in some way by using the fact that if there are two or one changePositions, then you cannot have 3 consectuve digit replacemenets (one must be divisible by three because it rotates through mod 3)
#This would imply that the most in a prime family would be 0,1,_,3,4,_,6,7,_,9 i.e. 7 primes. To get 8 primes, we must have the number of changepositions being a multiple of 3.
