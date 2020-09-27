n="294"
a=[[""],[""],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
l=len(n)
key=list()
for i in range(0,l):
    m=int(n[i])
    key.append(a[m][0])

for i in range(0,l-1):
    for j in range(i+1,i+2):
        n1=int(n[i])
        n2=int(n[j])
        if(n1>len(a[n2])):
            key.append(a[n2][n1%len(a[n2])-1])
        else:
            key.append(a[n2][n1-1])
print(key)

t=[]
for i in key:
    if (i not in t):
        t.append(i)
print(t)
print((len(t)))



