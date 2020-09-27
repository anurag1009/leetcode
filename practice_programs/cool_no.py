def check(s,k):
    c=0
    for i in range(0,len(s)-2):
       if s[i:i+3]=="101":
           c+=1
    if(c>=k):
        return 1
    else:
        return 0

tc=int(eval(input()))
while(tc!=0):
    l=list(map(int,input().split(" ")))
    r,k=l[0],l[1]
    count=0
    for j in range(1,r+1):
        s1=bin(j)
        s=s1[2:]
        if(check(s,k)==1):
            count+=1
    print(count)
    tc-=1


