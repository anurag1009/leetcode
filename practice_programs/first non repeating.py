s="aabccb"
k=0
for i in s:
    if s.count(i)==1:
        k+=1
        print(i)
        break
if k==0:
    print(-1)
