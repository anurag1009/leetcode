def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    return fact

num=int(raw_input("Enter a no."))
temp=num
sum=0
while(temp>0):
    rem=temp%10
    fact=factorial(rem)
    sum=sum+fact
    temp=temp/10
print sum
if(sum==num):
    print "YES"
else:
    print "NO"
