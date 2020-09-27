def prime(n):
    p=[2]
    for i in range(3,n+1):
        f=0
        for j in range(2,i):
            if(i%j==0):
                f+=1
        if(f==0):
            p.append(i)
    return p

n=78
pf=prime(n)
m=1
for i in pf:
    if(n%i==0):
        m=m*i
print m