n=int(input())
for i in range(0,n):
    l=list(map(int,input().split(" ")))
    sum=l[0]*(l[0]+1)*0.5
    if(l[1]==sum):
        print("1")
    else:
        print("0")

