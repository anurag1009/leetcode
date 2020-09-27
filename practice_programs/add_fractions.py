def lcm(a,b):
    t1=a*b
    r=1
    while(r>0):
        r=b%a
        b=a
        a=r
    hcf=b
    lc=int(t1/hcf)
    return(lc)

(n1,d1,n2,d2)=raw_input("enter-").split()
n1=int(n1)
d1=int(d1)
n2=int(n2)
d2=int(d2)
if(d1>=d2):
    D=lcm(d2,d1)
else:
    D=lcm(d1,d2)
N=int((D/d1)*n1 + (D/d2)*n2)
N=str(N)
D=str(D)
res=N+"/"+D
print(res)