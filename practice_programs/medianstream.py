n=eval(input("no. of elements:"))
a=[]
for i in range(n):
    a.append(eval(input("Enter elements")))
n=len(a)
for i in range(0,n):
    p=a[:i+1]
    p.sort()
    if((i+1)%2!=0):
        print(p[i//2])
    else:
        k=(p[i//2]+p[(i//2)+1])//2
        print(k)
