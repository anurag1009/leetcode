n=int(input())
l=list(map(int,raw_input().split(" ")))
z=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if l[i]+l[j]+l[k]==0 :
                z=1
                break
            else:
                pass
if z==1:
    print("1")
else:
    print("0")
