#Coin Sums

#How many different ways can £2 be made using any number of coins?
#The coins available are 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

#We calculate this inductively, starting with the number of ways to make 1p and working our way up.
#The only thing we have to be careful about is double counting 

import functools
from operator import add

coins = [1,2,5,10,20,50,100,200]

#We write a function that produces the number of coin breakdowns of a number and a list of coins
# by reducing it to either a lower number or a smallest list of coins

@functools.cache
def coin_breakdowns(total : int, *coins) -> int:
    coinlist = list(coins)
    if total == 0:
        return 1
    if not coinlist:
        return 0
    coin = coinlist.pop()
    ways = 0
    for i in range(0, total//coin + 1):
        ways += coin_breakdowns(total - i*coin, *coinlist)
        
    return ways

if __name__ == "__main__":
    print(coin_breakdowns(200, *coins))