def check(n):
    s=str(n)
    l=len(s)
    k=0
    for i in range(0,l-1):
        #if(abs(int(s[i+1])-int(s[i]))==1):
        if((int(s[i])+1== int(s[i+1])) or (int(s[i])-1== int(s[i+1]))):
            k+=1
    if (k==l-1):
        return 1
    else:
        return 0
j=int(eval(input()))
while j!=0:
    n=int(input())

    if(n//10==0 or n==10):
        for x in range(0, n + 1):
            print((x), end=' ')
    else:
        for x in range(0,11):
            print((x), end=' ')
        for i in range(11,n+1):
            if(check(i)==1):
                print((i), end=' ')
    j-=1