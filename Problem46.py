#Goldbach's Other Conjecture

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from Utils.Primes import Primes

def double_squares_lt(n):
    i = 1
    while (sq := 2*i*i) <= n:
        yield sq
        i += 1

def primes_lt(n,primes_list):
    i = 0
    while (prime := primes_list[i]) <= n:
        yield prime
        i += 1

def can_be_written(n,primes_list):
    for sq in double_squares_lt(n):
        for primes in primes_lt(n,primes_list):
            if sq + primes == n:
                return True
    return False


if __name__ == '__main__':
    max_check_until = 1000000

    primes = Primes()
    primes.upto(max_check_until)

    odd_composites = set(range(9,max_check_until,2)) - set(primes.list)

    for composite in odd_composites:
        if not can_be_written(composite,primes.list):
            print(composite)
            break
    
            