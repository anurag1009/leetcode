def fun(s, n):
    if (n == 1):
        print(s)
        return
    l = len(s)
    a = [[" " for x in range(l)] for y in range(n)]
    print(a)
    row = 0
    for i in range(l):

        # put characters in the matrix
        a[row][i] = s[i]
        if row == n - 1:
            down = False
        elif row == 0:
            down = True
        if down == True:
            row = row + 1
        else:
            row = row - 1
    #print(a)

    for i in range(n):
        for j in range(l):
            print(str(a[i][j]), end=" ")
        print()


s = "geeksforgeeks"
n = 4
fun(s, n)
