#Number Letter Counts
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

#For practice we try to use the repr magic function in a class.

digits = {1 : "One"
         ,2 : "Two"
         ,3 : "Three"
         ,4 : "Four"
         ,5 : "Five"
         ,6 : "Six"
         ,7 : "Seven"
         ,8 : "Eight"
         ,9 : "Nine"}

tens =  {1 : "Ten"
        ,2 : "Twenty"
        ,3 : "Thirty"
        ,4 : "Forty"
        ,5 : "Fifty"
        ,6 : "Sixty"
        ,7 : "Seventy"
        ,8 : "Eighty"
        ,9 : "Ninety"}

teens = {1 : "Eleven"
        ,2 : "Twelve"
        ,3 : "Thirteen"
        ,4 : "Fourteen"
        ,5 : "Fifteen"
        ,6 : "Sixteen"
        ,7 : "Seventeen"
        ,8 : "Eighteen"
        ,9 : "Nineteen"}

def digitsToNumber(x1,x2,x3,x4):
    string = ""
    if x1:
        string += digits[x1]
        string += " Thousand "
        if (not x2) and (x3 or x4):
            string += "and "
    if x2:
        string += digits[x2]
        string += " Hundred"
        if (x3 or x4):
            string += " and "
    if x3 == 1 and x4:
        string += teens[x4]
    elif x3: 
        string += tens[x3]
        string += " "
    if x3 != 1 and x4: 
        string += digits[x4]
    return string


class Number:
    def __init__(self, num):
        self.num = num
    
    def __repr__(self) -> str:
        num = self.num
        x4 = num % 10
        num //= 10
        x3 = num % 10
        num //= 10
        x2 = num % 10
        num //= 10
        x1 = num % 10
        num //= 10
        return digitsToNumber(x1,x2,x3,x4)

def numberGenerator(n):
    for i in range(1,n+1):
        yield Number(i)

total = 0
for i in numberGenerator(1000):
    print(str(i))
    total += len(str(i).replace(" ",""))

print(f"The number of characters needed to spell out all numbers 1 to 1000 is {total}")

