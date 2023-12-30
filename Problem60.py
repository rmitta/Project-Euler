#Prime Pair Sets

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

#The difficulty level of this problem suggests that our prime lister must be VERY efficient.
#I suggest really using the fact that you don't have to check primes above sqrt(n) for n.

#Let's try with our current primes algorithm.
#We start with a brute force systen where we try all combinations up to a certain prime.
#We have to be careful what our maximum allowed prime is, to ensure that we have calculated 
# every prime up to the repeat of that prime. 

from Utils.Primes import Primes
import itertools

def concatInts(x,y):
    return x * (10 ** len(str(y))) + y

#MAKE SURE THAT PRIMESLIST IS A SET - THIS MAKES LOOKUP O(1)
def isPairSet(group,primesList : set) -> bool:
    for pair in itertools.permutations(group,2):
        if not (concatInts(*pair) in primesList):
            return False
    return True

#The problem is that groups increases exponentially with size(primesBelowMax).
#How can we mitigate this?
#For instance, we can remove 2 because we know it will never work...
# is there a modulo 3 concept we can use? knowing that if you concatInts they add their mod 3 values.
# That means you cannot have a 1 and a 2 mod 3 in the same group!
# So we can pre-split our primesBelowMax into a 0/1 mod 3 and a 0/2 mod 3 group. 

def primesBelowMax(primesList,max):
    return [p for p in primesList if (2 < p) and (p < max)]

def splitPrimesListByMod3(primesList,max):
    primesBelowMax = [p for p in primesList if (3 < p) and (p < max)]
    return [3] + [p for p in primesBelowMax if p % 3 == 1], [3] + [p for p in primesBelowMax if p % 3 == 2]

def getPrimePairs(primesList,primesBelowMax):
    groups = itertools.combinations(primesBelowMax, 2)
    primePairSets = []
    for group in groups:
        if isPairSet(group,primesList):
            primePairSets.append(set(group))
    return primePairSets

def getPrimeTriples(primePairSets):
    primeTriples = []
    pastPairs = primePairSets
    while pastPairs:
        (x,_) = pastPairs[0]
        xPairs = [set(pair) for pair in pastPairs if x in pair]
        otherPairs = [set(pair) for pair in pastPairs if x not in pair]
        xPairedSingletons = [pair - {x} for pair in xPairs]
        xPairedNumbers = {num for [num] in xPairedSingletons}
        for (y,z) in otherPairs:
            if (y in xPairedNumbers) and (z in xPairedNumbers):
                primeTriples.append({x,y,z})
        pastPairs = otherPairs #Remove all occurences of x from remaining pairs.
    return primeTriples

def getPrimeQuadruples(primeTriples):
    primeQuadruples = []
    pastTriples = primeTriples
    while pastTriples:
        (x,_,_) = pastTriples[0]
        xTriples = [set(triple) for triple in pastTriples if x in triple]
        otherTriples = [set(triple) for triple in pastTriples if x not in triple]  
        xTriplesPairs = [triple - {x} for triple in xTriples]
        xFullTriples = getPrimeTriples(xTriplesPairs)
        primeQuadruples += [triple.union({x}) for triple in xFullTriples]
        pastTriples = otherTriples
    return primeQuadruples

def getPrimeQuintuples(primeQuandruples):
    primeQuintuples = []
    pastQuadruples = primeQuandruples
    while pastQuadruples:
        (x,_,_,_) = pastQuadruples[0]
        xQuadruples = [set(t) for t in pastQuadruples if x in t]
        otherQuadruples = [set(t) for t in pastQuadruples if x not in t]
        xQuadruplesTriples = [t - {x} for t in xQuadruples]
        xFullQuadruples = getPrimeQuadruples(xQuadruplesTriples)
        primeQuintuples += [quad.union({x}) for quad in xFullQuadruples]
        pastQuadruples = otherQuadruples
    return primeQuintuples

from time import time

t1 = time()

primes = Primes()
primes.upto(100000000)
primes.checked
primesList = set(primes.list)

primesToLookAt = primesBelowMax(primesList,10000)

pairs = getPrimePairs(primesList,primesToLookAt)
triples = getPrimeTriples(pairs)
quadruples = getPrimeQuadruples(triples)
quintuples = getPrimeQuintuples(quadruples)

sum(quintuples[0])

t2 = time()
print(t2-t1)
