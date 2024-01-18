#Truncatable Primes

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#(2,3,5 and 7) are not considered to be truncatable primes.

# Notes:
# Truncating from the right shows that no digit can be even (except the leftmost digit)

# We are given that there are only 11 of them: so we do not need to prove why, only to search until 
# we find all 11. 

from Utils.Primes import Primes
from Utils.Decorators import timed

def truncations(n) -> list[int]:
    digits = str(n)
    return [int(digits[i:]) for i in range(len(digits)) ] \
         + [int(digits[:i+1]) for i in range(len(digits)-1)]

@timed         
def main():
    primes = Primes()
    primes.upto(1000000)
    total = 0
    num_truncatable_primes = 0
    primes_set = set(primes.list)
    for p in primes.list[4:]: #Intentionally skip the 1 digit primes
        digits = str(p)
        if all(int(d) % 2 == 1 for d in digits[1:]): #Check: only the first digit can be even
            if digits[0] not in {1,4,6,8,9}: #First digit can't be 1,4 6 or 8 or 9
                if all(trunc in primes_set for trunc in truncations(p)):
                    total += p
                    num_truncatable_primes += 1
    print(num_truncatable_primes)
    print(total)
                
            
if __name__ == '__main__':
    main()