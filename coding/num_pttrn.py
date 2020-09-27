n=4
for i in range(n,0,-1):
    for j in range(0,2*i-1):
        print(i,end="")
    print()

for k in range(2,n+1):
    for l in range(0,2*k):
        print(k,end="")
    print()


"""n=4
for i in range(n,0,-1):
    print((2*i-1)*str(i))
for j in range(2,n+1):
    print((2*j)*str(j))"""
"""k,l=1,1
o,e=1,4
odd=[]
even=[]
while k<=n:
    odd.append(o)
    k+=1
    o+=2
while l<=n-1:
    even.append(e)
    e+=2
    l+=1

for i in range(n,0,-1):
    print((odd[i-1])*str(i))
for j in range(2,n+1):
    print((even[j-2]*str(j)))
n=4
i=n
odd=0
k=n-1
j=2
even=4
while(i>=0):
    print((i+k)*str(i))
    i-=1
    k-=1

while(j<=n):
    print((even) * str(j))
    j+=1
    even+=2"""



