s=input()
maximum=0
c=0
for i in s:
    if i in ['a','e','i','o','u']:
        c+=1
    else:
        maximum=max(c,maximum)
        c=0
print(maximum)