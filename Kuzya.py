F = [0] * (n + 1)
F[0] = 1
F[1] = F[0]
F[2] = F[1] + F[0]
for i in range(3, n + 1):
    F[i] = F[i - 3] + F[i — 2] + F[i — 1]
