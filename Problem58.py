#Spiral Primes
#See Project Euler website for problem details.

#Instead of creating an object which attempts to maintain the structural information of the spiral,
# we simply note the formulas for the numbers lying on the diagonals:
from Utils.Primes import Primes

def diagonals():
    sideLength = 2
    num = 1
    yield 1
    while True:
        for _ in range(4):
            num += sideLength
            yield num
        sideLength += 2

primes = Primes()
primes.extend(1000) #Just to start

numPrimes = 0
totalDiagonals = 1
ratio = numPrimes/totalDiagonals
sides = 1
diags = diagonals()
first = next(diags)

while (ratio >= .1) or numPrimes == 0:
    sides += 2
    for _ in range(4):
        nextDiag = next(diags)
        while nextDiag > (primes.list[-1]**2):
            primes.extend(1000,chunkSize=10000)
        if not any([nextDiag % prime == 0 for prime in primes.list]):
            numPrimes += 1
        if nextDiag in primes.list:
            numPrimes += 1
        totalDiagonals += 1
    ratio = numPrimes/totalDiagonals

print(f"The side length is {sides} when the ratio of primes along diagonals falls back below 10%")




