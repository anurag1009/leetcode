s=input()
l=[]
i=0
m=0
for i in s:
    if i not in l:
        l.append(i)
    else:
        mx=max(m,len(l))
        m=len(l)
        l.clear()
        l.append(i)
print(mx)
