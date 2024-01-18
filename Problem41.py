#Pandigital Prime

#What is the largest n-digit pandigital prime that exists?

#Helpfully, we can note that since digit sums must not be divisible by 3, a 8- or 9-digit pandigital
# prime is not possible. So we only have to check up to 7 digits long. 

from Utils.Primes import Primes


def is_pandigital(n : int) -> bool:
    """Checks if n is pandigital. Assumes that n is at most 9 digits long.
    """
    digits = str(n)
    return all(str(d) in digits for d in range(1,len(digits)+1))

def main() -> None:
    primes = Primes()
    primes.upto(10000000)
    for p in reversed(primes.list):
        if is_pandigital(p):
            print(p)
            break
        
if __name__ == "__main__":
    main()