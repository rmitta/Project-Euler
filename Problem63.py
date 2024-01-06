#Powerful Digit Counts

#How many n-digit positive integers exist which are also an nth power?

"""
We note immediately that 10**n is an (n+1) digit number, and so we rule out any m**n for m >= 10

We also note that for m < 10, as n increases eventually m**n must have less than n digits.

We can therefore solve this by checking, for each of 1 <= m <= 9, how many n's there are before 
m**n has less than n digits - we start with n=1 which works for all the m's, and increase n 
until the first time it fails. The total number of pairs (n,m) for which it works is our answer
"""

def works(n,m):
    return 10**(n-1) <= m**n < 10**n

count = 0
for m in range(1,10):
    n = 1
    while works(n,m):
        count += 1
        n += 1

print(count)