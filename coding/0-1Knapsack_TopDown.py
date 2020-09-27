wt=[1,3,4,5]
n=len(wt)
val=[1,4,5,7]
W=7
t=[[0]*(W+1)]*(n+1)
print(t)
for i in range(1,n+1):
    for j in range(1,W+1):
        if wt[i-1]<=j:
            t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
        else:
            t[i][j]=t[i-1][j]
print(t[n][W])
print(t)