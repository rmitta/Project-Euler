#Cubic Permutations

#Find the smallest cube for which exactly five permutations of its digits are cube.


#First approach idea: calculate all cubes of a fixed length,
# reduce each cube to it's digit count. 
# ask how many of each digit count there are. (find 5)

def cubed(n):
    return n**3

def cubesBetween(lower, upper):
    """Generates all cubes between the lower and upper limits given"""
    n = 1
    x = cubed(n)
    while x < lower:
        n += 1
        x = cubed(n)
    while x <= upper:
        yield x
        n += 1
        x = cubed(n)

def main():
    power = 1
    while True:
        cubes = [(sorted(list(str(cube))),cube) for cube in cubesBetween(10**power,10**(power+1) -1)]

        for (digits,cube) in cubes:
            a = list(filter(lambda x : x[0] == digits , cubes))
            if len(a) == 5:
                return (digits, cube)

        power += 1






