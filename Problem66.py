#Diophantine Equation=

#See project euler for description. 

"""
Essentially, our job is to create a fast diophantine equation solver that finds 
minimal solutions in x for x**2 - Dy**2 = 1

Then we find the D <= 1000 which yields the largest minimal solution value of x"""

#Speedup ideas:
# D even => x odd
# D odd => (x and y have opposite parity)

#We can also look at mod 3, since squares mod 3 are either 0 or 1
#i.e., x = 0 mod 3 => Dy**2 = 2 mod 3 => y**2 = 1 mod 3 and D = 2 mod 3
#also, x = 1 mod 3 => Dy**2 = 0 mod 3 => either y = 0 mod 3 or D = 0 mod 3
# What about from d?
# D = 0 mod 3 => x = 1 mod 3
# D = 1 mod 3 => options based on y

#Generally, D = 0 mod n => x**2 = 1 mod n
#For n prime, we get that x = += 1 mod n. So we could take the prime factorization of d to 
# significantly reduce the number of x's that we have to check! 
#It should be possible to calculate all the sqrts of 1 mod n for general n given the prime factorizaiton....


import math

#First attempt: 
def solve_diophantine_minimal(d):
    x = 1
    diff = 1
    if d % 2 == 2:
        diff = 2
    while True:
        y = solve_diophantine_minimal_fixed_x(d,x)
        if y:
            return (x,y,d)    
        x += diff
        if (x == 10) or (x == 100) or (x == 1000) or (x == 10000) or (x == 100000) or (x == 1000000) or (x == 10000000) or (x == 100000000) or (x == 1000000000):
            print(x)
    

def solve_diophantine_minimal_fixed_x(d,x):
    quotient, remainder = divmod(x**2 - 1, d)
    if remainder == 0:
        if (root := math.isqrt(quotient))**2 == quotient:
            return root
    return 0
        

for d in range(1,1001):
    if not math.isqrt(d)**2 == d:
        print(solve_diophantine_minimal(d))

#Gets stuck on d = 61. ~40 seconds to check up to 100000000

solve_diophantine_minimal(61)


#Second idea: Instead of using isqrt to check exactly whether we can get x**2 - 1 / D to be a squre,
# we consider two sides: x**2 and Dy**2 + 1. We increase x by 1, then if the other side is lower we 
# increase y until the first time that it is higher.

def solve_diophantine_minimal_2(d):
    x = 1
    y = 1
    lhs = x**2
    rhs = d*y**2 + 1
    while lhs != rhs:
        x += 1
        lhs = x**2 #! Note this is not the fastest, could improve with the help of maths by just adding
        while lhs > rhs:
            y += 1
            rhs = d*y**2 + 1
        if (x == 10) or (x == 100) or (x == 1000) or (x == 10000) or (x == 100000) or (x == 1000000) or (x == 10000000) or (x == 100000000) or (x == 1000000000):
            print(x)
    return (x,y,d)

solve_diophantine_minimal_2(61)
# ~25 seconds to check up to 100000000

def solve_diophantine_minimal_3(d):
    x = 1
    y = 1
    lhs = x**2
    rhs = d*y**2 + 1
    while lhs != rhs:
        lhs += 2*x + 1
        x += 1
        while lhs > rhs:
            rhs += d*(2*y + 1)
            y += 1
        if (x == 10) or (x == 100) or (x == 1000) or (x == 10000) or (x == 100000) or (x == 1000000) or (x == 10000000) or (x == 100000000) or (x == 1000000000):
            print(x)
    return (x,y,d)

for d in range(65,81):
    solve_diophantine_minimal_2(d)
#~23 seconds to check up to 100000000