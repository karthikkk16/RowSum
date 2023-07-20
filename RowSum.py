def RowSum(matrix,row,column):
    res=[]
    for i in range(row):
        sum=0
        for j in range(column):
            sum+=matrix[i][j]
        res.append(sum)
    return res

matrix=[]
row=int(input("Enter number of rows : "))
column=int(input("Enter number of columns : "))
for i in range(row):
    matrix.append(list(map(int,input().split())))

print(RowSum(matrix,row,column))