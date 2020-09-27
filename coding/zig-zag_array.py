l=[4,3,7,8,6,2,1]
#l=[1,4,3,2]
flag=1
for i in range(0,len(l)-1):
    if l[i]>l[i+1] and flag==1:
        l[i],l[i+1]=l[i+1],l[i]
    if l[i+1]>l[i] and flag==0:
        l[i+1],l[i] = l[i],l[i+1]
    flag= not flag
print(l)
