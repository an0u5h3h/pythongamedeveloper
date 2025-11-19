row=int(input("Enter the total amount of rows: "))
column=int(input("Enter the total amount of columns: "))
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

print("diagonal elements:")
for i in range(row):
    print(matrix1[i][i])

sumOfElements=0
for i in range(row):
    sumOfElements+=matrix1[i][i]
print('the sum of the diagonal elements is:', sumOfElements)
