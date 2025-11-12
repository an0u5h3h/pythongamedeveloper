matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)          # prints the entire matrix
print(len(matrix))     # prints the number of rows in the matrix
print(len(matrix[0]))  # prints the number of colomns in a row 
print(matrix[2][0])  # prints the element at 3rd row and 1st column
print(matrix[1][1])  # prints the elements on 2nd row and 2nd column 

for i in range(0,len(matrix)):     # for loop for row
    for j in range(0,len(matrix[0])):   # for loop for colomns
        print(matrix[i][j],end="  ")    # end tells python what to put at the end of the statement
    print("\n") # new line


print("hello world","it's me", "happy days",sep="-") # '-' is used to seperate different \ multiple string statements in a print function,

#take an input for the matrix and then print all the elements
row=int(input("Enter the total amount of rows we need: "))
column=int(input("Enter the total amount of columns we need: "))
matrix1=[]
for i in range(row):
    sublist=[]
    for j in range(column):
        x=int(input("enter a number: "))
        sublist.append(x)
    matrix1.append(sublist)
print(matrix1)
for i in range(row):
    for j in range(column):
        print(matrix1[i][j], end=" ")
    print("\n")
    
# adding and subtracting from the matrix
matrixa=[[1,2],[3,4]]
matrixb=[[5,6],[7,8]]
resulta=[[0,0],[0,0]] #using 0 as we dont know values (addition)
results=[[0,0],[0,0]] #subtraction
for i in range(0,2):
    for j in range(0,2):
        resulta[i][j]=matrixa[i][j]+matrixb[i][j]
        results[i][j]=matrixb[i][j]-matrixa[i][j]
for i in range(0,2):
    for j in range(0,2):
        print(resulta[i][j], end=" ")
    print("\n")
for i in range(0,2):
    for j in range(0,2):
        print(results[i][j], end=" ")
    print("\n")

#mulitplying 2dlists
matrixa=[[1,2],[3,4]]
matrixb=[[5,6],[7,8]]
result2=[[0,0],[0,0]]
for i in range(0,2):   #rows of matrixa
    for j in range(0,2): #columns of matrixb
        for k in range(0,2): #columns of matrixa should be the same of that of row 
            result2[i][j]=result2[i][j]+(matrixa[i][k]*matrixb[k][j])
for i in range(0,2):
    for j in range(0,2):
        print(result2[i][j], end=" ")
    print("\n")