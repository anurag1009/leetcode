s=input()
l=[]
i=0
mx=0
f=0
for i in s:
    if i not in l:
        l.append(i)
        #f+=1
    else:
        l.clear()
        l.append(i)
        #f=1
    mx=max(mx,len(l))
print(mx)
"""
input-geeksforgeeks
output-7 (for string eksforg)

input-aabcd
output-4 (for the string abcd)
"""