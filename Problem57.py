#Square Root Convergents

#In the first one-thousand expansions (of sqrt(2) as an infinite continued fraction), 
# how many fractions contain a numerator with more digits than the denominator?

import Utils

class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def add_one(self):
        self.num += self.den
        return self

    def invert(self):
        self.num, self.den = self.den, self.num
        return self
    
    def __repr__(self) -> str:
        return f"{self.num} / {self.den}"

@Utils.memoise
def root2frac(n):
    if n == 0:
        return Fraction(3,2)
    return root2frac(n-1).add_one().invert().add_one()

ans = 0
for i in range(1000):
    frac = root2frac(i)
    if len(str(frac.num))  > len(str(frac.den)) :
        ans += 1

print(f"{ans} fractions contain a numerator with more digits than the denominator")