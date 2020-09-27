l=[1,[2,3],[4,5,6,7,8],[9],[10,11],12,[13]]
f=l[::-1]
r=[]
for i in f:
    if type(i)==list:
        r.append(i[::-1])
    else:
        r.append(i)
print(r)
