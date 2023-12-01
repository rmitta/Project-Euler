#Prime Digit Replacements
#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

#

def replaceDigits(num,digit,positions):
    digitList = [int(x) for x in str(num)]
    newDigitList = [digit if index in positions else digitList[index] for index in range(len(digitList))]
    newStringDigitList = [str(digit) for digit in newDigitList]
    return int("".join(newStringDigitList))

def digitReplaceFamily(num,positions):
    return [replaceDigits(num,digit,positions) for digit in range(1,10)]

def allDigitReplaceFamilies(num):
    for numChanges in range(1,len(num)+1):
        



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
