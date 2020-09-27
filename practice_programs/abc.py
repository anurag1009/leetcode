l=["1","11"]
n=5
i=0
s=""
while i<len(l[-1])-1:
    k=0
    if l[i]==l[i+1]:
        k+=1
    else:
        s=str(k)+l[i]
        l.append(s)
print(l)