import itertools
ar=[1,3,5]
dep=[2,6,8]
k=1
l=[]

for i in range(len(ar)):
    l.append((ar[i],1))
    l.append((dep[i],0))
l.sort()

curr_active=max_active=0

for i in range(len(l)):
    if l[i][1]==1:
        curr_active+=1
        max_active=max(curr_active,max_active)

        if max_active>k:
            print("false")
            exit()
    else:
        curr_active-=1
print("true")

