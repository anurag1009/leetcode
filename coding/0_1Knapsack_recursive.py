def knapsack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    elif wt[n-1]<=W:
        return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
    else:
        return knapsack(wt,val,W,n-1)

wt=[1,3,4,5]
val=[1,4,5,7]
n=len(wt)
W=7
print(knapsack(wt,val,W,n))