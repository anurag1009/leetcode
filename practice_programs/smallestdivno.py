def check(li,num):
    for i in li:
        if(num%i!=0):
            return 0
    return 1

nums=list()
n=list()
r=int(raw_input("Enter no. of testcases-"))
for x in range(0,r):
    nums.append(int(raw_input(".")))

for y in range(0,len(nums)):
    for z in range(1,nums[y]+1):
        n.append(z)

    n.sort(reverse=1)
    t=n[0]
    #print n
    i=1
    s=1
    while(check(n,s)!=1):
        s=t*i
        i+=1
    print s
