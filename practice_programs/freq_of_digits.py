s = input("enter a string-")
n = len(s)
for i in range(0, 10):
    t = 0
    for j in range(0, n):
        if (s[j] == (str(i))):
            t += 1
    print(t, end=' ')



