tc=int(input())
while tc!=0:
    f=[]
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(0,n-1):
        if l[i]>=max(l[i+1:]):
            f.append(l[i])
    f.append(l[-1])
    print(f)
tc-=1
