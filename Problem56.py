#Powerful Digit Sum
#Considering natural numbers of the form, a**b, where a,b<100 what is the maximum digital sum?

maxSum = 0

def digitSum(num):
    string = str(num)
    return sum([int(i) for i in string])

for i in range(1,100):
    for j in range(1,100):
        maxSum = max(maxSum, digitSum(i**j))

print(maxSum)

