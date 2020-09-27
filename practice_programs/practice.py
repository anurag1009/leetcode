s="3(a)2(bh)1(abc)"
n1=""
i=0
while i<=len(s):
    if s[i] != '(':
        n1=n1+s[i]
        i+=1
        n=int(n1)
        n=n%10
    else:
        k=i+1
        ch=""
        while(s[k]!=')'):
            ch=ch+s[k]
            k+=1
            i=i+k
        while(n>0):
            print(ch, end=' ')
            n-=1



