sc=[100,100,50,40,40,20,10]
al=[5,25,50,120]
res=[]
tmp=[]
for i in range(0,len(al)):
    sc.append(al[i])
    sc.sort(reverse=True)
    tmp.append(1)
    for j in range(1,len(sc)):
        if sc[j-1]==sc[j]:
            tmp.append(tmp[j-1])
        else:
            tmp.append(tmp[j-1]+1)
    res.append(tmp[sc.index(al[i])])
    sc.remove(al[i])
    tmp.clear()
print(res)






