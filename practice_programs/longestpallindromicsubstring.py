#s="aaaabbaa"
#s="rfkqyuqfjkxy"
s="abcrzrwab"
n=len(s)
#print n
t=""
p=""
i=1
j=n-1
while i<n//2:
    p=s[i:]
    print(p,"aa")
    if p==p[::-1]:
        print(p,"done2")
        break
    else:
        while j>n//2+1:
            t=p[i:j]
            print(t,"bb")
            if t==t[::-1]:
                print(t,"done2")
                break
            j-=1
    i+=1
