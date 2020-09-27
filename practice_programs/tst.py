"""a=[1,2,3,4,5,6]
s=7
n=len(a)
for i in range(0,n-1):
    for j in range(i+1,n):
        if(a[i]+a[j]==s):
            print a[i],a[j]
"""

p=[0,0]
n=10
i=3
while(len(p)<n):
    if(i%2==0):
        m=p[-1]/2
        p.append(m)
        i+=1
    else:
        k=i-1
        p.append(k)
        i+=1
print p

