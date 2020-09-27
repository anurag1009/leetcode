s="hello"
res=""
for i in range(0,len(s)):
    m=ord(s[i])+i+1
    res=res+chr(m)
print res
