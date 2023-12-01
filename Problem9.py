#Special Pythagorean Triplet
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for a in range(1,500):
    for b in range(a+1,500):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 :
            print("{}, {}, {}".format(a,b,c))
            print(a*b*c)
