l=[2,3,6,5,8,9,13]
l.sort()
i=2
r=[l[0],l[1]]
k=0
while i<len(l):
    s=r[-1]+r[-2]
    if s in l:
        k+=1
        r.append(s)
        i=l.index(s)
    i+=1
if(k>0):
    print(r)
else:
    print("none")