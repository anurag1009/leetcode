l=list(map(str,input().split()))
l1=l.copy()
f=[]

for i in l:
    if i not in f:
        f.append(i)
        l1.remove(i)
    else:
        f.append(i+str(l.count(i)-l1.count(i)))
        l1.remove(i)
print(f)
