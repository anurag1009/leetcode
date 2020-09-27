s="a-fS-Z0-4"  #input format
f=""
for i in range(0,len(s)):
    if s[i]=="-":
        for j in range(ord(s[i-1]),ord(s[i+1])+1):
            f=f+chr(j)
print(f)