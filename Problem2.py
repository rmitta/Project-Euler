#Even Fibonacci Numbers
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#We define a fibonnaci matrix that functions to generate the next two fibonnaci numbers when an array of the previous two numbers is multiplied into it.
#Then we simply run through the fibonnaci numbers, checking to see if they are even, and adding those to the sum until we are at 4 million.

#Note: Actually every third fibonnaci number is even. We could have used this which may have made the algorithm ever so slighly faster.

import numpy as np

fibMat = np.array([[1,1],[1,0]])
fibNums = np.array([1,1])
sum = 0
while fibNums[0] <= 4000000:
    nextFib = fibNums[0]
    if nextFib % 2 == 0:
        sum += nextFib
    fibNums = np.matmul(fibNums,fibMat)

print(sum)