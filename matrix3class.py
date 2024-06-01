#Create python file
#It should contain three functions:
    #1 - add_matrix: adds any 2 matrices
    #2 - subtract_matrix: subtract any 2 matrices
    #3 - multiply_matrix: multiply any 2 matrices

#Note:
    #- The number of columns of the 1st matrix
    #must equal the number of rows of the 2nd
    #matrix.
    #- And the result will have the same number of
    #rows as the 1st matrix, and
    #the same number of columns as the 2nd matrix.


#1 - add_matrix: adds any 2 matrices

def print_matrix(matrixs):
    print()
    for i in range(3):
        for j in range(3):
            print(matrixs[i][j], end=" ")
        print()



matrix1 = [[1,5,10],[2,7,11],[12,3,7]]
matrix2 = [[2,4,6],[15,3,2],[4,8,1]]

matrix_result = [[2,4,6],[15,3,2],[4,8,1]]

def add_matrix(matrix_a, matrix_b):
    
    for i in range(3):
        for j in range(3):
            #print(i, " ", j)
            matrix_result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    
            
print_matrix(matrix1)
print_matrix(matrix2)
add_matrix(matrix1,matrix2)

print_matrix(matrix_result)

#2 - subtract_matrix: subtract any 2 matrices

    

