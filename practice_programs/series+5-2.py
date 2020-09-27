a=raw_input("enter-").split(" ")
p=list(map(int,a))
n1=p[0]
n2=p[1]
num=[]
num.append(n1)
for i in range(1,n2):
    if(i%2!=0):
        num.append(num[i-1]+5)
    else:
        num.append(num[i-1]-2)
print num ,
