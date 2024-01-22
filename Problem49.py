#Prime Permutations

#See project euler for question. 

"""Note that the last digit of the term difference must be
even. And the digit sum must be a multiple of 3"""

"""Probably the fastest way to search through our options is to look at possible 
prime pairs for the first two numbers, and then check if the required third 
number is prime."""

from Utils.Primes import Primes

primes = Primes()
primes.upto(10000)

four_digit_primes = [p for p in primes.list if 1000 <= p < 10000]

#Define a function that returns the first index in a list where the element is greater than 5000

def are_permutations(p1,p2):
    return sorted(list(str(p1))) == sorted(list(str(p2)))

def main():
    for i in range(len(four_digit_primes)):
        primei = four_digit_primes[i]
        for j in range(i+1,len(four_digit_primes)):
            primej = four_digit_primes[j]
            if are_permutations(primei,primej):
                primek = 2*four_digit_primes[j] - four_digit_primes[i]
                if are_permutations(primei,primek) and (primek in four_digit_primes):
                    print(four_digit_primes[i],four_digit_primes[j],2*four_digit_primes[j] - four_digit_primes[i])

if __name__ == "__main__":
    main()