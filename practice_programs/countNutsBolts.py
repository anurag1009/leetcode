l=['!','#','$','%','&','*','@','^','~']
tc=int(input())
while(tc!=0):
    n=int(input())
    s1=list(input().split())
    s2=list(input().split())

    p=""
    for i in range(len(l)):
        if l[i] in s1 and l[i] in s2:
            p=p+l[i]+" "
    print(p)
    print(p)
    tc-=1