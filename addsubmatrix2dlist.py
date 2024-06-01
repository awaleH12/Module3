matrix1=[[12 , 10 , 0] ,[4  , 5  , 7] ,[0  , 6  , 5]]


matrix2=[[9 , 1 , 9 ],[7 , 2 , 3 ] ,[8 , 5 , 0 ]]

print(matrix1)
print(matrix2)






for j in range(3):
    for i in range(3):
        matrix3=(matrix1[i][j] + matrix2[i][j])
        print(matrix3,end="\t   ")

print()    

for j in range(3):
    for i in range(3):
        matrix3=(matrix1[i][j] - matrix2[i][j] )
        print(matrix3,end="\t   ")

print()
