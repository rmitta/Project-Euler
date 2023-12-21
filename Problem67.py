#Maximum Path Sum II
#Find the maximum total from top to bottom in problem67_triangle.txt 

#USAGE: python problem67.py problem67_triangle.txt
import sys

def get_triangle(string : str):
    rows = string.split("\n")
    triangle = [row.split(" ") for row in rows]
    return [[int(x) for x in row] for row in triangle]

args = sys.argv
filename = args[1]
with open(filename, 'r') as f:
    data = f.read()
    print(type(data))
triangle = get_triangle(data)

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

obj = Triangle(triangle)
obj.findMaxs()
print(obj.maxs[0][0])