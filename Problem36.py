#Double-base Palindromes

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2

def is_palindromic_base_10(n):
    digits = str(n)
    return digits == digits[::-1]

def to_base_2_str(n):
    return bin(n)[2:]

def is_palindromic_base_2(n):
    digits = to_base_2_str(n)
    return digits == digits[::-1]

def is_double_palindromic(n):
    return is_palindromic_base_10(n) and is_palindromic_base_2(n)

def main():
    total = 0
    for i in range(1, 1000000):
        if is_double_palindromic(i):
            total += i
    print(total)

if __name__ == '__main__':
    main()   