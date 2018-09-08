C = [0] * (n + 1)
C[1] = Price[1]
Prev[1] = 0
for i in range(2, n + 1):
    if C[i — 1] < C[i — 2]:
        C[i] = C[i — 1] + Price[i]
        Prev[i] = i — 1
    else:
        C[i] = C[i — 2] + Price[i]
        Prev[i] = i — 2
