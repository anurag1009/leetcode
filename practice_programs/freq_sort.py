from collections import OrderedDict
tc=int(eval(input()))
while(tc!=0):
    n=int(eval(input()))
    l=list(map(int,input().split(" ")))
    l1=[]
    l2=[]
    d=OrderedDict()
    for k in l:
        if k not in l1:
            l1.append(k)
        l1.sort()
        d={}
    for i in l1:
        l2.append(l.count(i))
        d[i]=l.count(i)
    s=""
    for j in sorted(d,key=d.get,reverse=True):
        s+=str(j)*d[k]
    print((' '.join(s)))
tc-=1
#d={1: 7, 2: 7, 3: 6, 4: 3, 5: 4, 6: 3, 7: 7}

#print(sorted(d,key=d.get,reverse=True))
