#Even Fibonacci Numbers
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Could do this via 1 1, 1 0 matrix multiplication. Cute. 
#Just keep a running sum, while loop for exceeding 4M.

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