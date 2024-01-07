#Non-Abundant Sums

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#(with the knowledge that all integers greater than 28123 can be written as the sum of two abundant numbers)
import math
ceiling = 28123

#Plan: find all abundant numbers up to 28123. We already have d() which calculates the sum of divisors. 
# sum that with itself to find all abundant sums
# the ones we don't find are the non-abundant ones, which we then sum. 


def proper_divisors(n):
    divs = [1]
    for i in range(2,math.isqrt(n) + 1):
        if n % i == 0:
            divs.append(i)
            a = n // i
            if a != i:
                divs.append(a)
    return divs

def d(n):
    return sum(proper_divisors(n))

def abundant_numbers(upto):
    return [i for i in range(1,upto+1) if d(i) > i]

abundant_numbers_list = abundant_numbers(ceiling)
abundant_sums = {x + y for x in abundant_numbers_list for y in abundant_numbers_list}
print(sum(a for a in range(1,ceiling+1) if a not in abundant_sums))



