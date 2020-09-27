p1=[3]
p2=[7]
n=int(input("Enter-"))
for i in range(1,n):
    p1.append(p1[i-1]+p2[i-1])
    #print p1 ,
    p2.append(p2[i-1]+4)
print(p1[-1])

