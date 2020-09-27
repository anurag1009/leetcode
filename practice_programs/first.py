def merge(left,right):
    i,j=(0,0)
    res=[]

    while (i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                    res.append(left[i])
                    i+=1
            else:
                    res.append(right[j])
                    j+=1
    res+=left[i:]
    res+=right[j:]
    return res

def merge_sort(nums):
    if (len(nums)==1) :
            return nums
    else:
            mid=int(len(nums)/2)
            left=merge_sort(nums[:mid])
            right=merge_sort(nums[mid:])
            return merge(left,right)


#Main driver program
#arr=[5,6,0,-8,45]

n=eval(input("Enter range::"))
print("Enter the nos---")
arr=[]
for x in range(0,n):
    elem=eval(input())
    arr.append(elem)
print("The sorted numbers are")
sorted=merge_sort(arr)
print(sorted)

