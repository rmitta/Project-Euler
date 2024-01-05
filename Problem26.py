#Reciprocal Cycles

#Find the value of d < 1000 for which 1d contains the longest recurring cycle in its decimal fraction part.

#Our function repeatedly multiplies the numerator by 10 and then integer divides by d. Then it stores the 


def decimal_representation(d):
    n = 1
    #should we use two lists or an ordered dictionary?
    history = []
    results = []
    while True:
        history.append(n)
        n *= 10
        (a,r) = divmod(n,d)
        results.append(a)
        if r == 0:
            return results
        if r in history:
            return results, history.index(r)
        n = r

def main():
    best_d = 0
    greatest_cycle = 0
    best_frac = ()
    for d in range(2,1000):
        result = decimal_representation(d)
        if isinstance(result, tuple):
            cycle_len = len(result[0]) - result[1]
            if cycle_len > greatest_cycle:
                best_d = d
                greatest_cycle = cycle_len
                best_frac = result
    
    print(cycle_len, best_d, best_frac)


if __name__ == "__main__":
    main()