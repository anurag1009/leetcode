l=[5,81,1]
#l=[378674,908975,673229,54296,493106]
#l=[1119683,466340,790991,347288,632036,214073,272678,1223639]
n=len(l)
s=sum(l)/n
s1=str(s)
less,more=0,0
if n==1:
    print(0)
elif s1[-2:]!=".0":
    print(-1)
else:
    for i in l:
        if i<s:
            less=less+(s-i)
        if i>s:
            more=more+(i-s)
    if less==more and less%3==0:
        f=str(less//3)
        print(f[:-2])
    else:
        print(-1)
