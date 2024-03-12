#This is a more challenging version of Problem 81

#Path Sum: Three Ways

##Find the minimal path sum from any cell in the left column to any cell in the right column by only moving right, up and down in matrix.txt


"""
Once again this problem should be solved by iterating over columns 
- we solve the smaller problem at each step of how to get from any cell in one column to any cell in the next"""


# NOTE base case = column 
import numpy as np

with open('Problem82_matrix.txt',mode = 'r') as f:
    text_matrix = f.read().strip()

matrix = np.array([[int(digits) for digits in line.split(",")] for line in text_matrix.split('\n')])

class PathSum3():
    def __init__(self, matrix) -> None:
        self.n_rows,self.n_columns = matrix.shape
        self.columns = dict()
        for column_ind in range(self.n_columns):
            self.columns[column_ind] = Column(matrix[:,column_ind])
            
    def min_path_sum(self) -> int:
        for column_ind in range(self.n_columns)[::-1]:
            if column_ind == self.n_columns - 1:
                self.columns[column_ind].calculate_pathlens(np.zeros(self.n_rows))
            else:
                self.columns[column_ind].calculate_pathlens(self.columns[column_ind+1].pathlens)
        return min(self.columns[0].pathlens)

class Column():
    def __init__(self,column) -> None:
        self.entries = column
        self.pathlens = None
    
    def calculate_pathlens(self,previous_pathlens):
        self.pathlens = previous_pathlens + self.entries #the paths that connect straight
        #now we check to see if going up or down reduces any pathlens
        #first, if going down reduces any pathlens:
        for i in range(len(self.pathlens)-1):
            self.pathlens[i+1] = min(self.pathlens[i+1], self.pathlens[i] + self.entries[i+1])
        #then, if going up reduces any pathlens:
        for i in range(len(self.pathlens)-1)[::-1]:
            self.pathlens[i] = min(self.pathlens[i], self.pathlens[i+1] + self.entries[i])
            
problem = PathSum3(matrix)
print(problem.min_path_sum())