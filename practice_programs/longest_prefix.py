s=list(map(str,input().split()))
min=999
z=0
for i in range(len(s)):
    if len(s[i])<min:
        min=len(s[i])
        z=i

count=0
if (len(s) == 1):
    print((s[0]))

elif(len(s)==2):
    for j in range(len(s[z])):
        for k in range(0, len(s) - 1):
            if s[k][:j + 1] == s[k+1][:j + 1]:
                count += 1
else:
    for j in range(len(s[z])):
        for k in range(1,len(s)-1):
            if s[k-1][:j+1]==s[k][:j+1] and s[k-1][:j+1]==s[k+1][:j+1]:
                count+=1

print(count)
print((s[z][:count]))