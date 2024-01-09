# Digit Cancelling Fractions

# See project euler for details

import math
import numpy as np


class Fraction():
    def __init__(self, num : int, den : int):
        self.num : int = num
        self.den : int = den

    def add_digit_lr(self, digit):
        return Fraction(10*digit + self.num, digit + 10*self.den)

    def add_digit_rl(self, digit):
        return Fraction(10*self.num + digit, self.den + 10*digit)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def simplify(self):
        gcd = math.gcd(self.num, self.den)
        return Fraction(self.num // gcd, self.den // gcd)

    def __repr__(self) -> str:
        return f"{self.num} / {self.den}"


if __name__ == '__main__':
    non_trivial_digit_cancelling_fractions = []

    for den in range(1, 10):
        for num in range(1, den):
            baseFraction = Fraction(num, den)
            for digit in range(1, 10):
                add_lr = baseFraction.add_digit_lr(digit)
                if baseFraction == add_lr:
                    non_trivial_digit_cancelling_fractions.append(add_lr)
            for digit in range(1, 10):
                add_rl = baseFraction.add_digit_rl(digit)
                if baseFraction == add_rl:
                    non_trivial_digit_cancelling_fractions.append(add_rl)

    product_of_fractions = Fraction(np.product([frac.num for frac in non_trivial_digit_cancelling_fractions], dtype=int), 
                                    np.product([frac.den for frac in non_trivial_digit_cancelling_fractions], dtype=int))

    print(product_of_fractions.simplify().den)
