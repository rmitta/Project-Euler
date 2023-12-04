#Permuted Multiples
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

#For later: 2x and 6x must have the same number of digits. (Optimization)
#So 2x must clearly be between 1000.. and 3333..
#So x must be between 500.. and 1666...

def multiplesHaveSameDigits(x):
    digits = sorted([digit for digit in str(2*x)])
    for i in [3,4,5,6]:
        if digits != sorted([digit for digit in str(i*x)]):
            return False
    return True

def solve():
    x = 1
    found = False
    while not found:
        x += 1
        found = multiplesHaveSameDigits(x)
    return x

print(solve())
