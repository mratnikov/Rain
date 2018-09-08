C = [0] * (n + 1)
C[1] = Price[1]
for i in range(2, n + 1):
    С[i] = min(C[i — 1], C[i — 2]) + Price[i]
