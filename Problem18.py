#Maximum Path Sum 1
#Find the maximum total from top to bottom of the triangle below:

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def get_triangle(string):
    rows = string.split("\n")
    triangle = [row.split(" ") for row in rows]
    return [[int(x) for x in row] for row in triangle]    

#Lets write a problem that does this calculation from the bottom up, storing the max total at each 
# row so that we only have to check two paths per number.
#We will make a copy of the triangle array which we will use to store the max totals as we calculate our way up the triangle.

class Triangle():
    def __init__(self, rowlists):
        self._length = len(rowlists)
        self.rows = rowlists
        self.maxs = [[None for _ in row] for row in rowlists]
    
    def findMaxs(self):
        self.maxs[self._length-1] = self.rows[self._length-1]
        for row in range(self._length-2, -1, -1):
            for i in range(len(self.maxs[row])):
                if not self.maxs[row][i]:
                    self.maxs[row][i] = self.rows[row][i] + max(self.maxs[row+1][i],self.maxs[row+1][i+1])

obj = Triangle(get_triangle(triangle))
obj.findMaxs()
print(obj.maxs[0][0])
