#Path Sum: Two Ways

#Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt

with open('Problem81_matrix.txt',"r") as f:
    text_matrix = f.read().strip()

matrix = [[int(digits) for digits in line.split(",")] for line in text_matrix.split('\n')]

#When you can only move right or down, the matrix should be viewed as a diamond where at each step you 
# can move down one and right or left. (and then at some point only inwards)

#We should be able to solve this problem with some backpropagation of the minimum path.

#The diamond is organised in ranks by the sum of the indices.

height = len(matrix) - 1
width = len(matrix[0]) - 1
max_rank = height + width

min_path_matrix = [[0 for _ in line] for line in matrix]

#Initialize min_path_matrix with the final element of matrix
min_path_matrix[-1][-1] = matrix[-1][-1]

#Loop through each rank and backpropogate the minimum path to get there.
for rank in range(max_rank-1, -1, -1):
    for i in range(max(0,rank-height), min(rank+1,height+1)):
        j = rank - i
        if i == height:
            min_path_matrix[i][j] = min_path_matrix[i][j+1] + matrix[i][j]
        elif j == width:
            min_path_matrix[i][j] = min_path_matrix[i+1][j] + matrix[i][j]
        else:
            min_path_matrix[i][j] = min(min_path_matrix[i][j+1], min_path_matrix[i+1][j]) + matrix[i][j]

print(min_path_matrix[0][0])
