#Convergents of e

#Find the sum of digits in the numerator of the 100th convergent of the 
# continued fraction for e.

"""
Seems like there is no good way to calculate the nth convergent from the n-1th
convergent. So to calculate the nth convergent we need to calculate from the
bottom of the continued fraction back upwards."""

import fractions

def e_continued_fraction_gen():
    k = 1
    yield 2
    while True:
        yield 1
        yield 2*k
        yield 1
        k += 1

def nth_convergent(n):
    gen = e_continued_fraction_gen()
    e_continued_fraction = [next(gen) for _ in range(n)]
    
    frac = fractions.Fraction(e_continued_fraction[-1])
    for next_value in reversed(e_continued_fraction[:-1]):
        frac **= -1
        frac += fractions.Fraction(next_value)

    return frac

def digit_sum(n):
    return sum(int(digit) for digit in str(n))    

if __name__ == '__main__':
    print(digit_sum(nth_convergent(100).numerator))

