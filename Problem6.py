#Sum Square Difference
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#By expanding and simplifying the equation we find that the difference is equal to:
# sum_(i=2..n) sum(j=1..(i-1)) (2*i*j)

sumSquareDifference = sum([2*i*j for i in range(2,101) for j in range(1,i)])

print(sumSquareDifference)