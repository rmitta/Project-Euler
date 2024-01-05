#Lexicographic Permutations

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

p = permutations(range(10),10)

for _ in range(999999):
    _ = next(p)
next(p)
