matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)          # prints the entire matrix
print(len(matrix))     # prints the number of rows in the matrix
print(len(matrix[0]))  # prints the number of colomns in a row 
print(matrix[2][0])  # prints the element at 3rd row and 1st column
print(matrix[1][1]) 

for i in range(0,len(matrix)):     # for loop for row
    for j in range(0,len(matrix[0])):   # for loop for colomns
        print(matrix[i][j],end="  ")    # end tells python what to put at the end of the statement
    print("\n") # new line


print("hello world","it's me", "happy days",sep="-") # '-' is used to seperate different \ multiple string statements in a print function,