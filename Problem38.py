#Pandigital Multiples

#See Project Euler for Question

"""
The brute force method: note that n can only range from 2 to 9, otherwise the concatenated
product would have more than 9 digits. Multiply and check for pandigital products until 
we go over 9 digits.   
"""

def contains_all_digits(n : str) -> bool:
    return all(d in n for d in "123456789")

def main():
    largest_pandigital_product = 0
    for n in range(2,10):
        too_large = False
        m = 1
        
        while too_large == False:
            product = [m * i for i in range(1,n+1)]
            product_str = ''.join(str(i) for i in product)
            if len(product_str) > 9:
                too_large = True
            if len(product_str) == 9:
                if contains_all_digits(product_str):
                    largest_pandigital_product = max(largest_pandigital_product, int(product_str))
                    
            m += 1
    print(largest_pandigital_product)

if __name__ == '__main__':
    main()
