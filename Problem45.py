#Triangular, Pentagonal, and Hexagonal

#Find the next triangle number that is also pentagonal and hexagonal. (after 40755)

def triangle_gen():
    n = 0
    while True:
        n += 1
        t = n * (n + 1) // 2
        yield t
        
def pentagonal_gen():
    n = 0
    while True:
        n += 1
        p = n * (3 * n - 1) // 2
        yield p
        
def hexagonal_gen():
    n = 0
    while True:
        n += 1
        h = n * (2 * n - 1)
        yield h

def match_gen():
    triangles = triangle_gen()
    pentagons = pentagonal_gen()
    hexagons = hexagonal_gen()
    t = next(triangles)
    p = next(pentagons)
    h = next(hexagons)
    while True:
        if t == p and t == h:
            yield t
        t = next(triangles)
        while p < t:
            p = next(pentagons)
        while h < t:
            h = next(hexagons)
        
def main(): 
    matches = match_gen()
    print(next(matches))
    print(next(matches))
    print(next(matches))
    
if __name__ == "__main__":
    main()