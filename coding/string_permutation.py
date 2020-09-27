def permutation(res, s, i, n):
    if i == n:
        res.append("".join(s))
    else:
        for j in range(i, n + 1):
            s[i], s[j] = s[j], s[i]
            permutation(res, s, i + 1, n)
            s[i], s[j] = s[j], s[i]  # backtrack to its original string


s = "1234"
res = []
permutation(res, list(s), 0, len(s) - 1)
print(sorted(res))