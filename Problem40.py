#Champernowne's Constant

#See Project Euler for Question.

import numpy as np

stack = []
digits_for_product = []
n = 0
i = 0

while i <= 1000000:
    
    if not stack:
        n += 1
        next_digits = reversed(str(n))
        for d in next_digits:
            stack.append(d)

    i += 1
    next_digit = stack.pop()
    if i in [1,10,100,1000,10000,100000,1000000]:
        digits_for_product.append(next_digit)
        
print(digits_for_product)
print(np.prod([int(digit) for digit in digits_for_product]))
    