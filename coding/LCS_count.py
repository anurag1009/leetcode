# #-------------LCS Recursive---------------#
# def lcs(x,y,m,n):
#     if m==0 or n==0:
#         return 0
#     elif x[m-1]==y[n-1]:
#         return 1+lcs(x,y,m-1,n-1)
#     else:
#         return max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))
#
# x="ABCDGH"
# y="AEDFHR"
# print(lcs(x,y,len(x),len(y)))

#--------------------LCS Memoized (bottom-up)-------------#

# def lcs(x,y,m,n):
#     if m==0 or n==0:
#         return 0
#     if t[m][n]!=-1:
#         return t[m][n]
#     if x[m-1]==y[n-1]:
#         t[m][n]=1+lcs(x,y,m-1,n-1)
#         return t[m][n]
#     t[m][n]=max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))
#     return t[m][n]
#
# x="ABCDGH"
# y="AEDFHR"
# m=len(x)
# n=len(y)
# t=[[-1]*(n+1)]*(m+1)
# lcs(x,y,m,n)
# print(t[m][n])



#--------------------LCS Memoized (top-down)-------------#
x="ABCDGH"
y="AEDFHR"
m=len(x)
n=len(y)
t=[[-1]*(n+1)]*(m+1)

for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            t[i][j]=0
        elif x[i-1]==y[j-1]:
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])
print(t[m][n])
####for printing the substring######
s=""
i=m
j=n
while i>0 and j>0:
    if x[i-1]==y[j-1]:
        s=x[i-1]+s
        i-=1
        j-=1
    else:
        if t[i-1][j]>t[i][j-1]:
            i-=1
        else:
            j-=1
print(s)

####################for  length of shortest common supersequence############################

# x="AGGTAB"
# y="GXTXAYB"
# trick--> first find the LCS bcoz that will be the part of supersequence then deduct that by total length of two strings
# i.e supersequence length is --> m+n-LCS

#################for finding min. no insertions and deletions to make a string x to string y################

#x="heap"
#y="pea"

#LCS--2 ("ea")

#again here also we can see that there is LCS involved because to change "heap" to "pea" first we have to make 2 deletions from
#"heap" i.e h and p then remaining is "ea" which is LCS and to that we have to insert one letter "p" to make it "pea"
#so total:
# deletions-->2 which is actually m-LCS (4-2)
# insertions--->1 which is actually n-LCS(3-2)

