def check(li,num):
    for i in li:
        if(num%i!=0):
            return 0
    return 1

n1=input("Enter nos.").split(" ")
n=list(map(int,n1))
n.sort(reverse=1)
t=n[0]
print(n)
i=1
s=1
while(check(n,s)!=1):
    s=t*i
    i+=1
print(s)
