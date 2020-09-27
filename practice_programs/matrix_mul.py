m = int(eval(input("Enter row1:")))
n = int(eval(input("Enter column1:")))
p = int(eval(input("Enter row2:")))
q = int(eval(input("Enter column2:")))
m1 = [[int(eval(input("Enter data for m1"))) for j in range(m)] for i in range(n)]
m2 = [[int(eval(input("Enter data for m2"))) for j in range(p)] for i in range(q)]
result = [[0 for j in range(m)] for i in range(q)]

if (n != p):
    print("multiplication not possible")

for i in range(m):
    for j in range(q):
        for k in range(n):
            result[i][j] += m1[i][k] * m2[k][j]

for i in range(m):
    for j in range(q):
        print(result[i][j], end=' ')
    print()
