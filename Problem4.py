#Largest Palindrome Product
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    digits = str(n)
    return digits == digits[::-1]

def largestPalProduct():
    largestPal = 0

    for i in range(100,1000):
        for j in range(100,i):
            p = i*j
            if isPalindrome(p):
                if p > largestPal:
                    largestPal = p
    return largestPal

print("Largest Palidrome Product of two 3-digit numbers: {}".format(largestPalProduct()))