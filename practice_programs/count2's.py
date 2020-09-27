c=[]
n=0
def div(x):
    while x!=0 :
        n=x%10
        c.append(n)
        x//=10
    return c
p=list()
for x in range(1,101):
    p=div(x)
print(p)

f=0
for i in p:
    if(i==2):
        f+=1
print(f)



"""n=10
p=[2]
c=3
while(len(p)<n):
    for j in range(3,c):
        if(c%j==0):
            break
    else:
        p.append(c)
    c+=2
print p """
