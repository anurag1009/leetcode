def dfs(l,i,j):
    r = len(l)
    c = len(l[0])
    if i>=0 and i<r and j>=0  and j<c and l[i][j]=='O':
        l[i][j]='@'
        dfs(l, i+1, j)
        dfs(l, i-1, j)
        dfs(l, i, j+1)
        dfs(l, i, j-1)

l=[ ['X','X','X','O','X'],
    ['X','X','O','X','O'],
    ['X','X','O','O','O'],
    ['O','X','X','X','X'],
    ['X','X','O','O','X'],
    ['X','X','X','X','X']]

r=len(l)
c=len(l[0])
for i in range(r):
    for j in range(c):
        if l[i][j]=='O' and (i==0 or i==r-1 or j==0 or j==c-1):
            dfs(l,i,j)
print(l)

for i in range(r):
    for j in range(c):
        if l[i][j]=='@':
            l[i][j]='O'
        elif l[i][j]=='O':
            l[i][j]='X'
print(l)