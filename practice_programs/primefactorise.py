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

n=350
i=0
pf=prime(n)
count=0
power=list()
while(n!=1):
    while(n%pf[i]==0):
        count+=1
        n=n/pf[i]
    power.append(count)
    count=0
    i+=1
#print(power)

s=""
for i in range(0,len(power)):
    if(power[i]>0):
        t1=str(power[i])
        t2=str(pf[i])
        s=s+"*"+t2+"^"+t1

print(s[1:])


