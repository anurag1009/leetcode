s=input("enter the size of matrix in MxN format")
r=int(input("enter the row no. of destination cell"))
c=int(input("enter the column no. of destination cell"))
m=int(s[0])
n=int(s[-1])
T=m*[n*[0]]
for p in range(0,r+1):
    for q in range(0,c+1):
        if p==0 or q==0:
            T[p][q]=1
        else:
            T[p][q]=T[p-1][q]+T[p][q-1] #N(Total ways)=N(upper cell)+N(left cell)
print(T[r][c])
