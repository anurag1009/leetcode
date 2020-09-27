n=int(raw_input("Enter of testcases:"))
for j in range(1,n+1):
    s=raw_input("Enter a sentence-").split(".")
    res=""
    for i in range(len(s)-1,-1,-1):
        res=res+"."+s[i]
    print res[1:]
