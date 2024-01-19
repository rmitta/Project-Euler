#Sub-string Divisibility

#Find the sum of all 0 to 9 pandigital numbers with this property.
#See Project Euler for property details.

import itertools

def substrings(digits : str, length = 3) -> list[int]:
    return [int(digits[i:i+length]) for i in range(0, len(digits) + 1 - length)]

def pandigitals_0_to_9():
    perms = itertools.permutations(range(0, 10), 10)    
    while True:
        try:
            n = next(perms)
        except StopIteration:
            break
        if n[0] != 0:
            if n[3] % 2 == 0: #The crucial two steps, vastly reducing the number of possibilities we have to search through.
                if n[5] % 5 == 0:
                    yield ''.join(str(n[i]) for i in range(10))

divisible_tests = {0 : 1,
                   1 : 2,
                   2 : 3,
                   3: 5,
                   4: 7,
                   5: 11,
                   6: 13,
                   7: 17}

def main():
    total = 0
    for n in pandigitals_0_to_9():
        subs = substrings(n)
        if all(subs[i] % divisible_tests[i] == 0 for i in range(8)):
            total += int(n)
    print(total)
    
if __name__ == "__main__":
    main()
     
    