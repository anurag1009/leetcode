l=[2,3,2,3,4,4,4,4,5]
static c=0;
for i in range(0,len(l)):
    s=l.count(l[i])
    if(s==l[i]):
        i=i+s
    else:
        j=i-s+1
        while(j<=(j+s)):
            del l[j]
            c+=1
            j+=1
print l
