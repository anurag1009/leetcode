n=3
for i in range(0,n):
    for k in range(0,i):
        print((" "), end=' ')
    for j in range(65+i,65+n):
        print((chr(j)), end=' ')
    for m in range(65+n-2,65+i-1,-1):
        print((chr(m)), end=' ')
    print()
