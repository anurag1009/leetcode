#s="asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
#t="asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
s="ashley"
t="ash"
k=3
#print(len(s),len(t))
if s==t and k>0:
    print("yes")
else:
    for i in range(0,min(len(s),len(t))):
        if s[i]!=t[i]:
            p=i
            print("match")
            break
        else:
            p=i
    print(p)
    print(len(s[p+1:]),len(t[p+1:]))
    op=len(s[p+1:])+len(t[p+1:])
    print(op)

    if op==k or (p==0 and op<k):
        print("Yes")
    else:
        print("no")
