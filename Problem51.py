#Prime Digit Replacements
#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

#
from itertools import combinations
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
        numChangeRange = range(3,numLength,3)
    else:
        numChangeRange = range(1,numLength)
    changes = []
    for numChanges in numChangeRange:
        changes += list(combinations(range(numLength),numChanges))
    return changes

def primesUpTo(n):
    primesList = []
    primes = np.ones(n+1, dtype=np.bool_)
    primes[0],primes[1] = False, False
    for p in range(2,n+1):
        if primes[p]:
            primesList.append(p)
            if 2*p <= n:
                for m in range(2*p,n+1,p):
                    primes[m] = False
    return primesList, primes

def checkPrimesList(primesList,primesBitArray):
    for prime in primesList:
        for positions in enumeratePositionOptions(len(str(prime))):
            family = digitReplaceFamily(prime,positions)
            primesInFamily = [x for x in family if primesBitArray[x]]
            if len(primesInFamily) >= 8:
                if len(str(primesInFamily[0])) == len(str(prime)):
                    return(primesInFamily)
    return "No 8 prime family found in primesList"

#checkPrimesList(primesUpTo(100000))
maxN = 10000000
primesList, primesBitArray = primesUpTo(maxN)
print(checkPrimesList(primesList,primesBitArray))

#Just realised we can reduce our search in some way by using the fact that if there are two or one changePositions, then you cannot have 3 consectuve digit replacemenets (one must be divisible by three because it rotates through mod 3)
#This would imply that the most in a prime family would be 0,1,_,3,4,_,6,7,_,9 i.e. 7 primes. To get 8 primes, we must have the number of changepositions being a multiple of 3.
#We can also reduce our seach by noting that the last digit of the prime cannot be changed, else we would 5 even (nonprime) numbers in the family.