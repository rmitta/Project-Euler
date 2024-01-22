#Self Powers

#Find the last ten digits of the series, 1**1 + 2**2 + ... + 1000*1000

"""The key thing to note here is that when calculating the values of each term n**n, we actually do
not care about the digits after the first 10. I.e we can take it modulus 10000000000 each time. 
"""

"""It turns out that for these values, the 'naive' approach is much faster.
For significantly larger values of n, the non-naive approach works better"""

def last_10_of_self_power_naive(n):
    return n**n % 10000000000
    
def last_10_of_self_power(n):
    ans = 1
    for i in range(n):
        ans *= n
        ans %= 10000000000
    return ans

def main():
    ans = sum(last_10_of_self_power_naive(i) for i in range(1,1001))
    print(ans % 10000000000)
    
if __name__ == "__main__":
    main()
    