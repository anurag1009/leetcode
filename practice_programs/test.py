s="geeksforgeeks"
s="theeare"
c=0
maximum=0
l=[a,e,i,o,u]
for i in s:
    if i in l:
        c+=1
    else:
        maximum=max(c,maximum)
        c=0
print maximum