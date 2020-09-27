def knapsack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if t[n][W]!=-1:
        return t[n][W]
    if wt[n-1]<=W:
        t[n][W]=max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
        return t[n][W]
    else:
        t[n][W]=knapsack(wt,val,W,n-1)
        return t[n][W]

wt=[1,3,4,5]
n=len(wt)
val=[1,4,5,7]
W=7
t=[[-1]*(W+1)]*(n+1)
print(knapsack(wt,val,W,n))
#print(t[n][W])
