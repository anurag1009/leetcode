"""The idea is to use a 2D array of size hash[MAX+1][2]

Algorithm:

Assign all the values of the hash matrix as 0.
Traverse the given array:
    If the element ele is non negative assign
        hash[ele][0] as 1.
    Else take the absolute value of ele and
         assign hash[ele][1] as 1.
To search any element x in the array.

If X is non-negative check if hash[X][0] is 1 or not. If hash[X][0] is one then the number is present else not present.
If X is negative take absolute value of X and then check if hash[X][1] is 1 or not. If hash[X][1] is one then the number is present"""

def insert(l,n):
    for i in l:
        if i>=0:
            hash_arr[i][0]=1
        else:
            hash_arr[abs(i)][1]=1
def search(x):
    if x>=0 and hash_arr[x][0]==1:
        return True
    x=abs(x)
    if hash_arr[x][1]==1:
        return True
    else:
        return False

l=list(map(int,input().split()))
MAX=max(l)+1
hash_arr=[[0 for i in range(2)] for j in range(MAX+1)]

insert(l,len(l))

print(hash_arr)
x=-5
if search(x):
    print("present")
else:
    print("not present")

