#Digit Factorials

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#(1 and 2 are not sums so are not included) (so start looking from 10?)


"""
The only question is how we can bound the numbers we have to search through.
We do this by noting that 9! = 362880 is the most a digit can contribute to the sum.
The highest we can sum with 7 digits is therefore 2540160, which is a 7 digit number. Any more digits
would increase the number faster than the sum, so this is a simple upper bound for 
numbers equal to the sum of the factorial of their digits.
"""

from math import factorial

lower_bound = 10
upper_bound = 2540160


#We do this so recalculating factorials is not needed. 
factorials = { str(n) : factorial(n) for n in range(0, 10) }

def sum_of_digit_factorials(n):
    return sum(factorials[n] for n in str(n))
    

if __name__ == "__main__":
    total = 0
    for n in range(lower_bound,upper_bound):
        if sum_of_digit_factorials(n) == n:
            total += n
    print(total)
        