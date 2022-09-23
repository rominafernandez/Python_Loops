## Exercise 25 - Loop trough a MatrixLoop

# Write a Program that uses nested loops to tackle the tasks below:
# Search for the coordinates of maximal value of the matrix
# Sum up all entries of the matrix
# Describe the multiplication of the components of two matrices in a third resulting matrix

my_list = []
my_matrix = []

for i in range(3):
    my_list.append(i)
for j in range(3):
    my_matrix.append(my_list)

# my_matrix = [[1,3,5],[2,4,6],[7,8,9]]

print(f"Here is the matrix: {my_matrix}")

# Coordinates of max value
max = 0
max_index = [0,0]

for i in list(range(len(my_matrix))):
    for j in list(range(len(my_matrix[i]))):
        if my_matrix[i][j] > max:
            max = my_matrix[i][j]
            max_index[0] = i
            max_index[1] = j
print(f"The max value of the matrix is {max} and first occurs at index {max_index}")

# Sum up matrix
sum = 0
for i in my_matrix:
    for j in i:
        sum = sum + j
print(f"The sum of all elements in the matrix is {sum}.")

# multiplicate two matrices
result_matrix = []

for i in list(range(len(my_matrix))):
    tmp = list(range(len(my_matrix[i])))
    for j in list(range(len(my_matrix[i]))):
        tmp[j] = my_matrix[i][j] * my_matrix[i][j]
    result_matrix.append(tmp)
print(f"The first matrix multiplicated by itself results in: {result_matrix}")
