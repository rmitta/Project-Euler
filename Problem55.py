#Lychrel Numbers
#How many Lychrel numbers are there below ten-thousand?
#Check Project Euler for full description

def flip(x: int) -> int:
    return int(''.join(list(reversed(str(x)))))

def isLychrel(x: int) -> bool:
    num = x
    flippedNum = flip(num)
    for i in range(50):
        num += flippedNum
        flippedNum = flip(num)
        if num == flippedNum:
            return False
    return True

count = 0
for i in range(1,10000):
    if isLychrel(i):
        count += 1

print(count)