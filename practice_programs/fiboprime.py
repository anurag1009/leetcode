def fib(n1):
    a = b = i = 1
    while (i <= n1):
        c = a + b
        a = b
        b = c
        i += 1
    return c


def prime(n2):
    p = [2]
    i = 3
    while (len(p) < n2):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            p.append(i)
        i += 2
    return (p[-1])


n = int(eval(input("enter a no.")))
if (n == 1 or n == 3):
    print((1))
    exit()
if (n % 2 == 0):
    m = int(n / 2)
    res = prime(m)
    print(res)
else:
    m = int(n / 2) + 1
    m = m - 2
    res = fib(m)
    print(res)