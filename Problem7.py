#10001st Prime
#What is the 10001st prime number?

def removeMultiplesOf(p,list):
    return [x for x in list if (x % p != 0)]

def primeList(n):
    primes = []
    intsChecked = 1
    potentialPrimes = []
    while len(primes) < n:
        #When necessary extend the range of our search
        if not potentialPrimes:
            potentialPrimes = list(range(intsChecked+1,intsChecked + 1001))
            intsChecked += 1000
            #Remove multiples of already checked primes
            for p in primes:
                potentialPrimes = removeMultiplesOf(p,potentialPrimes)
        
        #Main step: take next prime, add it to list, remove multiples.
        p = potentialPrimes.pop(0)
        primes.append(p)
        potentialPrimes = removeMultiplesOf(p,potentialPrimes)
    return primes

print("The 10001st prime number is {}".format(primeList(10001)[10000]))