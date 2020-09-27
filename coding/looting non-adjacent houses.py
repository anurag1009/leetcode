val=[5,3,4,11,2]
n=len(val)
dp=[0]*n
dp[0]=val[0]
dp[1]=max(val[0],val[1])

if n==0:
    print(0)
    exit()
if n==1:
    print(val[0])
    exit()
if n==2:
    print(max(val[0],val[1]))
    exit()
dp[0]=val[0]
dp[1]=max(val[0],val[1])

for i in range(2,n):
    dp[i]=max(val[i]+dp[i-2],dp[i-1])
print(dp[-1])