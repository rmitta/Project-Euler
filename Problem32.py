#Pandigital Products

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital

#So we need 9 digits to be used, note that 10 * 100 = 1000 uses 9 digits, so if we have 5 digits on
# multiplication side of the equality we must have at least 4, therefore 4 ont the right.
# on the other hand if we only use 4 digits on the left of the equality, the largest is
# 99 * 99 = 9081 which doesn't have enough total digits. 
# Conclusion: these products must be the product of a 2 and 3 digit number yeilding a 4 digit product.
# Or a 1 and a 4 digit number yielding a 4 digit number. 

#  That gives us the bounds to cycle through:
products = []
for i in range(10,100):
    for j in range(100,1000):
        m = i*j
        if 1000 <= m < 10000:
            if set(('1','2','3','4','5','6','7','8','9')) == (set(str(m))).union(set(str(i))).union(set(str(j))):
                products.append(m)

for i in range(1,10):
    for j in range(1000,10000):
        m = i*j
        if 1000 <= m < 10000:
            if set(('1','2','3','4','5','6','7','8','9')) == (set(str(m))).union(set(str(i))).union(set(str(j))):
                products.append(m)

print(sum(set(products)))

