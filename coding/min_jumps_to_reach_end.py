l=[1,3,5,8,9,2,6,7,6,8]
n=len(l)
min_jumps=[0 if p==0 else 99 for p in range(n)]
for i in range(1,n):
    for j in range(0,i):
        if i<=l[j]+j:
            min_jumps[i]=min(min_jumps[i],min_jumps[j]+1)
print(min_jumps[-1])