s1=raw_input("Enter a String1-")
s2=raw_input("Enter a String2-")
l1=len(s1)
l2=len(s2)
m=min(l1,l2)
s=""
for i in range(0,m):
    s=s+s1[i]+s2[i]
if(l1>l2):
    s=s+s1[m:]
else:
    s=s+s2[m:]
print(s)

