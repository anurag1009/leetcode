tc = int(input())
while tc != 0:
    n = int(input())
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    f = ""
    t=n
    while n > 0:
        r = n % 62
        print(r),
        f = f + s[r]
        n = n / 62
        print(n),
    print(f[::-1])
    print(t)
    tc -= 1
