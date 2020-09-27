s="sd&hg#j"
r=""
f=[]
for i in range(len(s)):
    if s[i].isalpha():
        r=r+s[i]
    else:
        f.append(i)
s1=list(r[::-1])
for j in f:
    s1.insert(j,s[j])
print(("".join(s1)))
