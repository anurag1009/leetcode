n=8
for i in range(1,n+1):
    for k in range(n-i,0,-1):
        print((" "), end=' ')
    for j in range(1,i+1):
        print((j), end=' ')
    for m in range(i-1,0,-1):
        print((m), end=' ')
    print()
