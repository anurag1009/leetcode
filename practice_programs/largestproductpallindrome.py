#n=int(raw_input())
n=2
l=int("1"+(n-1)*"0")
r=int("9"*n)
#print l,r
max=""
for i in range(r+1,l-1,-1):
    for j in range(r+1,l-1,-1):
        k=str(i*j)
        if k==k[::-1]:
            #max=k
            break
        break
print(max)


