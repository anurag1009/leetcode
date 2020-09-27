n=int(eval(input()))
s=0
s1=""
for i in range(n):
    s1=str(i)
    s=i+int(s1[::-1])
    if(s==n):
        print(i,int(s1[::-1]))
        break
