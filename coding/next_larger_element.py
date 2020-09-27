l=[1,3,2,4]
f=[]
k=1
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]>l[i] and k==1:
            f.append(l[j])
            k+=1
    if k==1:
        f.append(-1)
    k=1
f.append(-1)
print(f)