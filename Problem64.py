#Odd Period Square Roots

#How many continued fractions (of sqrt N) for N <= 10000 have an odd period?

#We use the method as described in https://proofwiki.org/wiki/Partial_Denominators_of_Continued_Fraction_Expansion_of_Irrational_Square_Root

from math import sqrt, isqrt, floor

def continued_fraction_root(n):
    integer_part_root = isqrt(n)
    A = []
    P = []
    Q = []
    PQ = []
    P.append(0)
    Q.append(1)
    PQ.append((P[0],Q[0]))
    A.append(integer_part_root)
    r = 0
    while True:
        r += 1
        P.append(A[r-1]*Q[r-1] - P[r-1])
        Q.append((n - P[r]**2) // Q[r-1]) #Noting there is a lemma to show that this division is integer
        PQ.append((P[r],Q[r]))
        try:
            A.append(floor((integer_part_root + P[r]) / Q[r]))
        except ZeroDivisionError:
            print(P[r], Q[r], n)
        if (r1 := PQ.index(PQ[r])) < r:
            break
    
    return A[:-1] , (r1,r)
            
def main():
    total = 0
    for n in range(1,10001):
        if sqrt(n) != isqrt(n):
            _, (r1,r) = continued_fraction_root(n)
            if r1-r % 2 == 1:
                total += 1
    print(total)

if __name__ == "__main__":
    main()