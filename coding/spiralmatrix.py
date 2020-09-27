def printspiral(m,n,matrix):
    k,l=0,0
    last_row=m-1
    last_col=n-1
    while(k<=last_row and l<=last_col):

        for i in range(l,last_col+1):
            print(matrix[k][i])
        k+=1

        for i in range(k,last_row+1):
            print(matrix[i][last_col])
        last_col-=1

        if(k<=last_row):
            for i in range(last_col,l-1,-1):
                print(matrix[last_row][i])
            last_row-=1
        if(l<=last_col):
            for i in range(last_row,k-1,-1):
                print(matrix[i][l])
            l+=1

matrix=[]
for i in range(0,3):
    l=list(map(int,input().split(" ")))
    matrix.append(l)
printspiral(3,3,matrix)




