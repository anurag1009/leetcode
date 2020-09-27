l=list(map(int,raw_input().split(" ")))

for i in range(0,len(l)):
     t=l[len(l)-i:]+l[:len(l)-i-1]