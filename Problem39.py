#Integer Right Triangles

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.
# For which value of p <= 1000, is the number of solutions maximised?

# We note that for each value of a there is at most one value of b (which therefore determines c) 
# that yields a right angle triangle of perimeter p.

#We could search by fixing p and, looking at each a and finding (if it exists) the b, c that 
# match. (Note that in this case we could use the value of b for a-1 as a starting point and search
# downwards from there to find the b)

#We could alternatively search by fixing a, searching b until p > 1000, and recording each instance.

import math

solutions = {p : [] for p in range(1,1001)}
for a in range(1,250):
    b = a+1
    while (c := math.sqrt(a**2 + b**2)) + a + b <= 1000:
        if c.is_integer():
            c = int(c)
            solutions[a+b+c].append((a,b,c))
        b += 1
            
print(max(range(1,len(solutions)+1), key=lambda i: len(solutions[i])))
