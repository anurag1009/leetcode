z =int(eval(input()))
while z!=0:
    n=eval(input())
    l = list(map(int, input().split()))
    mid=len(l)//2
    k=0
    if len(l) == 1:
        print("1")
    else:
        if sum(l[:mid]) < sum(l[mid+1:]):
            while mid != len(l):
                #print(l[:mid], l[mid+1:])
                if sum(l[:mid]) == sum(l[mid+1:]):
                    print((len(l[:mid])+1))
                    k+=1
                    break
                #print("IN Right",mid)
                mid+=1
        else:
            while mid != 1:
                #print(l[:mid], l[mid+1:])
                if sum(l[:mid]) == sum(l[mid+1:]):
                    print((len(l[:mid])+1))
                    k += 1
                    break
                #print("IN left",mid)
                mid-=1
        if k==0:
            print("-1")
    z-=1



"""tc=int(input())
while(tc!=0):
    n=int(input())
    l=list(map(int,raw_input().split()))
    c=0
    if(n==1):
        print "1"
    else:
        for i in range(1,n-2):
            print(i),
            if(sum(l[:i])==sum(l[i+1:])):
                c+=1
                print(i+1,"yoyo")
                break
        if(c==0):
            print("-1")
    tc-=1"""
