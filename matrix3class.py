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
matrix2 = [[2,5,3],[5,7,4],[1,9,7]]

matrix_result = [[0,0,0],[0,0,0],[0,0,0]]

def add_matrix(matrix_a, matrix_b):
    
    for i in range(3):
        for j in range(3):
            #print(i, " ", j)
            matrix_result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    
            
#print_matrix(matrix1)
#print_matrix(matrix2)
add_matrix(matrix1,matrix2)

print_matrix(matrix_result)

#2 - subtract_matrix: subtract any 2 matrices
print()  
matrix_subt_1 = [[1,5,10],[2,7,11],[12,3,7]]
matrix_subt_2 = [[2,5,3],[5,7,4],[1,9,7]]
def subtract_matrix(matrix_a, matrix_b):
    for i in range(3):
        for j in range(3):
            print(matrix_subt_1[i][j] - matrix_subt_2[i][j], end="\t")
        print()

subtract_matrix(matrix_subt_1,matrix_subt_2)


#3 - multiply_matrix: multiply any 2 matrices
print()
matrix_mult1 = [[1,5,10],[2,7,11],[12,3,7]]
matrix_mult2 = [[2,5,3],[5,7,4],[1,9,7]]
def multiply_matrix(matrix_a, matrix_b):
    for i in range(3):
        for j in range(3):
            print(matrix_mult1[i][j] * matrix_mult2[i][j], end="\t")
        print()
        
multiply_matrix(matrix_mult1,matrix_mult2)


