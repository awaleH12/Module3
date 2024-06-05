#1 - print as matrix
#2 - double all values
#3 - exchange rows and columns

matrix = [
    [12,  10,  0, 3],[4,   5,    7,  5],[0,   6,   5,  8],[9,   1,   9,  0]
    ]


print(matrix)

#1 - print as matrix
for i in range(4):
    for j in range(4):
        
        print(matrix[i][j], end="\t")
    print()




print()

#2 - double all values
for i in range(4):
    for j in range(4):
        print(matrix[i][j] *2, end="\t")
    print()
        




    

print()
#3 - exchange rows and columns
for row in range(4):
    for column in range(4):
         print(matrix[column][row], end="\t")
    print()
        


#print martix geting the data from user:
matrix2 = []
row = []
for i in range(4):
    input("Enter row matrix: ")
    row.append(i)
print(row)

    
column = []
for i in range(4):
    input("Enter column matrix: ")
    column.append(i)
print(column)

    
    
    



