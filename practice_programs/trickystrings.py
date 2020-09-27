n="ABCPQR"
a=list()
for i in n:
    a.append(ord(i))
print a

s=""
for i in range(0,len(a)-1):
    if((a[i+1]-a[i])==1):
        s=s+chr(a[i])+chr(a[i+1])
        print s
