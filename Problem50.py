#Consecutive Prime Sum

#Which prime, below one-million, can be written as the sum of the most *consecutive* primes?

from Utils.Primes import Primes

#We can do this by steadily increasing the number (of consecutive primes) that we search for. 

def how_many_primes_summed_before(n, primes_list):
    total = 0
    i = 0
    while total < n:
        total += primes_list[i]
        i += 1
    return i

def find_prime_sum_consecutive(num_consecutive,primes_list,primes_set):
    for start_index in range(len(primes_list)+1-num_consecutive):
        candidate = sum(primes_list[start_index:start_index+num_consecutive])
        if candidate in primes_set:
            return candidate, primes_list[start_index:start_index+num_consecutive]
        if candidate > primes_list[-1]:
            return None

def main(max_n):
    primes = Primes()
    primes.upto(max_n)
    primes_set = set(primes.list)
    
    num_consecutive = 21
    ans = ()
    
    for num_consecutive in range(21, how_many_primes_summed_before(max_n,primes.list)+1): 
        candidate = find_prime_sum_consecutive(num_consecutive,primes.list,primes_set)
        if candidate:
            ans = num_consecutive,candidate[0]
    print(ans)

if __name__ == '__main__':         
    main(1000000)