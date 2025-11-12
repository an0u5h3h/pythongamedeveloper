matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
#1. print the value in the first row & first column
print(matrix[0][0])

#2. print the value in the second row & third column
print(matrix[1][2])

#3. print the value in the last row and last colun using negative indices 
print(matrix[-1][-1]) #negative indices start with -1 on the last integer 

#4. store the value in matrix[1][1] into a variable named middle_value
middle_value=matrix[1][1]
print(middle_value)

#5. print the entire second row
print(matrix[1])

#6. print the entire third column only using indexing
print(matrix[0][2],matrix[1][2],matrix[2][2])

#7. use a for loop to print all the values in the second row
for i in range(len(matrix[1])):
    print(matrix[1][i], end=" ")
    print("\n")

#8. use nested loops to print all values in the matrix one per line
for i in range(len(matrix)):     # for loop for row
    for j in range(0,len(matrix[0])):   # for loop for colomns
        print(matrix[i][j])    # end tells python what to put at the end of the statement

#9. print all values in the first colum using a loop 
for i in range(len(matrix)):
    print(matrix[i][0])