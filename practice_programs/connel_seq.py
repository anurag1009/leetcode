n=15
i=1
p=[]

while(len(p)!=n):
    if(i%2!=0):
        if(len(p)==0):
            p.append(1)
            i+=1
        else:
            last=p[-1]+1
            s=0
            r=i
            while(s<r and len(p)!=n):
                #print last
                p.append(last)
                s+=1
                last+=2
            i+=1

    if(i%2==0):
        last=p[-1]+1
        t=0
        m=i
        while(t<m and len(p)!=n):
            #print last
            p.append(last)
            t+=1
            last+=2
        i+=1
print(p)