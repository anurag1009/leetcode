def pow1(a, b, c):
    if b == 0:
        print(c)
        return 1
    return a * pow1(a, b - 1, c + 1)


def pow2(a, b, c):
    if b == 0:
        print(c)
        return 1
    if b % 2 == 0:
        return pow2(a ** 2, b // 2, c + 1)
    else:
        return a * pow2(a, b - 1, c + 1)


print("pow1")
print(pow1(3, 100, 0))
print("pow2")
print(pow2(3, 100, 0))