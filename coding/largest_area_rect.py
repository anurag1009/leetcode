def NSL(arr):
    pseudoindex=-1
    stck=[]
    res=[]
    for i in range(len(arr)):
        if i==0:
            res.append(pseudoindex)
            stck.append([arr[i],i])
        else:
            while len(stck)>0 and stck[-1][0]>=arr[i]:
                stck.pop()
            if len(stck)==0:
                res.append(pseudoindex)
            else:
                res.append(stck[-1][1])
            stck.append([arr[i],i])
    return res

def NSR(arr):
    pseudoindex=len(arr)
    stck=[]
    res=[]
    for i in range(len(arr)-1,-1,-1):
        if i==len(arr)-1:
            res.append(pseudoindex)
            stck.append([arr[i],i])
        else:
            while len(stck)>0 and stck[-1][0]>=arr[i]:
                stck.pop()
            if len(stck)==0:
                res.append(pseudoindex)
            else:
                res.append(stck[-1][1])
            stck.append([arr[i],i])
    return res[::-1]

def MAH(t):
    left=NSL(t)
    right=NSR(t)
    area=[t[i]*(right[i]-left[i]-1) for i in range(len(t))]
    return(max(area))


matrix=[[0,1,1,0],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0]]
t=[matrix[0]]
res=[]
res.append(MAH([t[0][0]]))
p=[]

for i in range(1,len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            p.append(0)
        else:
            p.append(t[i-1][j]+matrix[i][j])
    t.append(p)
    p=[]
    res.append(MAH(t[i]))
print(max(res))



