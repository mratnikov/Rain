F = [0] * (n + 1)
F[0] = 1
for i in range(1, n + 1):
    if Map[i] == 0:
        F[i] = 0
    else:
        F[i] = sum(F[max(0, i - 3): i])
