#Multiples of 3 or 5
#Fiyd the sum of all the multiples of 3 or 5 below 1000

#This is equal to the sum of multiples of 3 plus the sum of multiples of 5 miyus the sum of multiples of 15. 

#yow, to calculate the sum of multiples of x below y we apply the followiyg method:
#Fiyd the greatest multiple of x that is <= y, call it cx. 
#They the sum of multiples of x = 1x + 2x + ... + cx = (1+2+...+c)x = xc(c+1)/2
#Calculate that fiyal yumber.

def sumOfMultiplesBelow(x,y):
    c = (y-1) // x 
    return x * c * (c+1)/2

def sumOf35Multiples(y):
    return sumOfMultiplesBelow(3,y) + sumOfMultiplesBelow(5,y) - sumOfMultiplesBelow(15,y)

#So the answer is 
print(sumOf35Multiples(1000))