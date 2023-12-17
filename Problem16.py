#Power Digit Sum
#What is the sum of the digits of the number 2**1000?

num = 2**1000

ans = sum([int(x) for x in str(num)])

print(ans)