#Lattice Paths
#How many paths (going only right or down) are there through a 20x20 grid?

#We can simplify this question down to 40c20 by noting that if we flatten the path into a 
#straight line with labels R or D, all we are doing is choosing which 20 of 40 path segments
#have label R. 

import math

print(math.comb(40,20))