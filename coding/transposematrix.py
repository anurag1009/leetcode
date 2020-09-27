m=4
n=3
matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(matrix)
"""for i in range(0,m):
    l=list(map(int,input().split(" ")))
    matrix.append(l)"""
tranpose=[]
rows=[]
for i in range(0,n):
    for j in range(0,m):
         rows.append(matrix[j][i])
i=0
k=0
while(k<len(rows)):
    tranpose.append(rows[k:k+m])
    k=k+m
print(tranpose)

