def _removeMultiplesOf(p,list):
    return [x for x in list if (x % p != 0)]

class Primes():
    """Stores lists of primes."""
    def __init__(self) -> None:
        self.list = []
        self.checked = 1
    
    #This is currently very slow since it checks chunks for primes that are greater than sqrt(chunkmax)
    def extend(self, n, chunkSize = 1000):
        """Extend the primeslist by n new primes. Searches chunks of chunkSize integers at a time."""
        potentialPrimes = []
        prevLen = len(self.list)
        while len(self.list) < prevLen + n:
            #When necessary extend the range of our search
            if not potentialPrimes:
                potentialPrimes = list(range(self.checked+1,self.checked + chunkSize + 1))
                self.checked += chunkSize
                #Remove multiples of already checked primes
                for p in self.list:
                    potentialPrimes = _removeMultiplesOf(p,potentialPrimes)

            #Main step: take next prime, add it to list, remove multiples.
            p = potentialPrimes.pop(0)
            self.list.append(p)
            potentialPrimes = _removeMultiplesOf(p,potentialPrimes)
            
        self.checked = self.list[-1] #Because the while loop cuts off halfway through a chunk.
    