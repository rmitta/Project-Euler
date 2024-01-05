#1000 digit Fibonacci Number

#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import numpy as np

fibMat = np.array([[1,1],[1,0]])
fibNums = np.array([1,1], dtype=object)

index = 2
while len(str(fibNums[0])) < 1000:
    fibNums = np.matmul(fibNums,fibMat)
    index += 1