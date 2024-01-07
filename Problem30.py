#Digit Fifth Powers

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_digit_fifth_powers(n: int) -> int:
    """
    This function returns the sum of the fifth powers of its digits.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    int: The sum of the fifth powers of its digits.
    """
    digit_powers = [int(d) ** 5 for d in str(n)]
    return sum(digit_powers)

def is_sum_digit_fifth_powers(n: int) -> bool:
    """
    This function checks if a number is equal to the sum of the fifth powers of its digits.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: Whether the number is the sum of the fifth powers of its digits.
    """
    return sum_digit_fifth_powers(n) == n

#We note that sum_digit_fifth_powers(999999) = 354294 which is < 999999, so clearly all numbers 
# greater than 999999 are not sums of the fifth powers of their digits.
# Therefore testing up to 999999 is enough.

if __name__ == '__main__':
    total = 0
    for n in range(2, 1000000):
        if is_sum_digit_fifth_powers(n):
            total += n
    print(total)   

