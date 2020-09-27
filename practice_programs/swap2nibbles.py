def bin_to_dec(s):
    dec=0
    l=len(s)
    for i in range(0,l):
        t=int(s[l-i-1])
        dec=dec+(2**i)*t
    return dec

n=int(input("Enter a decimal no-"))
s=bin(n)
s=s[2:]
for x in range(0,8-len(s)):
    s="0"+s
print(s)
m=int(len(s)/2)
swp=s[m:]+s[0:m]
final=bin_to_dec(swp)
print(final)
