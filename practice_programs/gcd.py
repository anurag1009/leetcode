def gcd(a,b):
    r=1
    while(r>0):
        r=b%a
        b=a
        a=r
    print(b)
gcd(9,6)
