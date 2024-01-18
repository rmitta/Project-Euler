#Circular Primes

#How many circular primes are there below one million?

from Utils.Primes import Primes
from Utils.Decorators import timed

primes = Primes()

primes.upto(1000000)
#primes.upto(100)

#We convert the list into a set for O(1) insert/lookup/delete operations. 
primes_set = set(tuple(primes.list))

def digit_rotations(n : int) -> list[int]:
    digits = str(n)
    return [int("".join((digits[n:], digits[:n]))) for n in range(len(digits))]

@timed
def main(primes_set):
    total = 1 #To get the prime set 2
    for n in primes.list:
        if all(int(d) % 2 == 1 for d in str(n)):
            if all(n in primes_set for n in digit_rotations(n)):
                total += 1
    return total

main(primes_set)
    


