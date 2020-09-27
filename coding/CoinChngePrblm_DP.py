coins=list(map(int,input().split()))
n=len(coins)
sum=int(input())
T=n*[(sum+1)*[0]]
for i in range(0,n):
    for j in range(0,sum+1):
        if i==0 and j==0:
            T[i][j]=1
        else:
            if coins[i]>j:
                T[i][j]=T[i-1][j]
            else:
                T[i][j]=T[i-1][j]+T[i][j-coins[i]]
print(T[n-1][sum])