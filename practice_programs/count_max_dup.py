s="hello assessment team"
l=list(s.split())
p=[]
ltr=""
word=""
for i in l:
    mx=-1
    for j in range(len(i)):
        if(i.count(i[j])>mx):
            mx=i.count(i[j])
            ltr=i[j]
            word=i
    p.append([mx,ltr,word])
print(p)
print((max(p)))
