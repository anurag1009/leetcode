s=input("Enter ")
res=""
k=0
for i in range(0,len(s)):
    p=ord(s[i])
    if(p>=65 and p<97):
        k=p+32
        res=res+chr(k)
    else:
        k=p-32
        res = res + chr(k)
print(res)