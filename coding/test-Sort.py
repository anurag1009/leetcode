def cmp(a,b):
    n1=str(a)+str(b)
    n2=str(b)+str(a)
    if n1>n2:
        return 1


l=[3,30,34,5,9]
l1=l.copy()
print(l1.sort())
print(sorted(l,key=cmp))