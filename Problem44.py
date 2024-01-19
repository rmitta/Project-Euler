#Pentagon Numbers

#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal 
# and D = |Pk - Pj| is minimised; what is the value of D?

def penta_gen():
    n = 0
    while True:
        n += 1
        p = n * (3 * n - 1) // 2
        yield p
        
def penta(n):
    p = n * (3 * n - 1) // 2
    return p

#Method: first we search for a single pair that satisfies this property. 
# Once we find that, we calculate their difference D.
# We find the first pentagonal number Pn such that Pn - P(n-1) is greater than D.
# Then Pn is the largest pentagonal number we need to look up to when searching for a possible smaller difference
# We calculate the set of pentagonal numbers up to 2*Pn (for the lookup set) and check all pairs up to
# Pn for smaller D. 

penta_set = set()
pentas = penta_gen()
p = next(pentas)
penta_set.add(p) 
p = next(pentas)
penta_set.add(p)

first_pair_found = False
n = 2

while not first_pair_found:
    n += 1
    pn = penta(n)
    #Extend penta_set up to at least 2*pn
    while p <= 2*pn:
        p = next(pentas)
        penta_set.add(p)
    
    #Check all pairs up to pn for the property
    for k in range(1,n):
        pk = penta(k)
        if ((pn - pk) in penta_set) and ((pn + pk) in penta_set):
            first_pair_found = True
            d = pn - pk
            
print(d)

#We find the first pentagonal number Pn such that Pn - P(n-1) is greater than d.
pn_prev = penta(n-1)
while pn - pn_prev < d:
    n += 1
    pn_prev = pn
    pn = penta(n)

#Extend penta_set up to a least 2*pn
while p <= 2*pn:
        p = next(pentas)
        penta_set.add(p)
        
#Check all pairs up to pn for the property (implementation repeats some calculation)
for j in range(1,n+1):
    pj = penta(j)
    for k in range(j-1,0,-1):
        pk = penta(k)
        if pj - pk >= d:
            break #since all other k's in this inner loops yield larger differences
        if ((pn - pk) in penta_set) and ((pn + pk) in penta_set):
            d = pj - pk
            
print(d)

#It turns out the first pair we find also has the smallest difference... 
    
    
    