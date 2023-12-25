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
    return int(str(x)+ str(y))

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

primes = Primes()
primes.extend(4500000,100000) #Goes beyond 34,170,000
primes.extend(1000000,1000000) #Goes beyond 34,170,000
primes.checked
primesList = set(primes.list)

primesToLookAt = primesBelowMax(primesList,7691)

pairs = getPrimePairs(primesList,primesToLookAt)
triples = getPrimeTriples(pairs)
quadruples = getPrimeQuadruples(triples)
quintuples = getPrimeQuintuples(quadruples)

#This method takes over a minute to run and doesn't find any quintuples. at 1057.

# def getNextSizeTuples(prevTuples):
#     nextTuples = []
#     pastTuples = prevTuples
#     pastTupleLength = len(pastTuples[0])
#     while pastTuples:
#         someTuple = pastTuples[0]
#         x = next(iter(someTuple))
#         xTuples = [set(t) for t in pastTuples if x in t]
#         otherTuples = [set(t) for t in pastTuples if x not in t]
#         xTuplesWOx = [t - {x} for t in xTuples]
#         if pastTupleLength == 2:
            
#         xFullTuples = getNextSizeTuples(xTuplesWOx)






#For the next round we can just recursively call the previous... I.e. take one x, form xTriples and otherTriples, , then call get PrimeTriples on xTriples...
    





#We pick the next number. We take all the pairs containing that number.
# we strip those sets of that number, forming a list.
# for each remainig pair in primePairSets, we check of both are in the list.
#   if so, that triple is in.
# we then remove all pairs containing that number. Repeat until none left. 


#


#We should maintain a list of all the possible primes here, and pop them, search through the options
#Or do we just search each pair of pairs for a match, and pop once we've completely searched one.

# def getPrimeTriples(primePairs):
#     primePairTriples = []
#     for x,y in itertools.combinations(primePairs,2):
#         for x1 in x:

        

#             if 
#         if x2 in (y1,y2):
#             #search (note that they cant both be)
        



# def nextSizeSets(prevSets,list):
#     for set in prevSets:
#         for n in list:
#             if n not in set:
#                 yield set,n

# def nextSizePrimePairSets(prevSets, primesList, max):
#     primesBelowMax = [p for p in primesList if p < max]
#     sets = nextSizeSets(prevSets,primesBelowMax)
#     primePairSets = []
#     for oldSet,n in sets:
#         if isPairSet((*oldSet,n),primesList):
#             primePairSets.append((*oldSet,n))
#     return primePairSets
    

# a = getPrimePairSets(2,primes.list,680)
# b = nextSizePrimePairSets(a,primes.list,680)
# c = nextSizePrimePairSets(b,primes.list,680)

#Error: getting multiple permations of the same, 
# also doing unnecessary checks that sets we already have are within themselves concatPrimes.


#In fact, the biggest step is simply the putting them into pairs step. Because after that we are actually just going to search for pairchains that make up the whole 5.

