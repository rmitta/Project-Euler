#Longest Collatz Sequence
#Which starting number, under one million, produces the longest Collatz Sequence chain?

class Collatz():
    def __init__(self, startInt) -> None:
        self.start = startInt
        self.value = startInt
        self.length = 1

    def step(self):
        self.length += 1
        x = self.value
        if (x % 2 == 0):
            self.value = x // 2
        else:
            self.value = 3*x + 1

def longestChainStartingBelow(n):
    maxLength = 0
    for startInt in range(1,n+1):
        chain = Collatz(startInt)
        while chain.value != 1:
            chain.step()
        if chain.length > maxLength:
            maxLength = chain.length
    return chain.start