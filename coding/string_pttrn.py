s="APPLE HP IBM MICROSOFT"
r=[]
l=s.split(" ")
#print(l)
m=0
for i in l:
    if m<len(i):
        m=len(i)
for i in l:
    s1=i+(m-len(i))*" "
    r.append(s1)
print(r)

for j in range(0,m):
    for k in range(0,len(r)):
        print(r[k][j],end="")
    print()

