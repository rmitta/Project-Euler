#Amicable Numbers

#Evaluate the sum of all the amicable numbers under 10000.

#Let's try first the most blunt force method:

def divisors(n):
    divs = []
    for i in range(1,n):
        if n % i == 0:
            divs.append(i)
    return divs

def d(n):
    return sum(divisors(n))

amicable = []
for n in range(1,10001):
    a = d(n)
    if a != n:
        b = d(a)
        if n == b:
            amicable.append(n)

sum(amicable)
