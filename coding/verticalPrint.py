s="apple hp ibm microsoft"
#n=s.count(" ")+1
l=s.split(" ")
m=0
for i in l:
    if len(i)>m:
        m=len(i)
l1=[]

for j in l:
    l1.append((m-len(j))*" "+j)
print(l1)

for k in range(m-1,-1,-1):
    print(l1[0][k],l1[1][k])







