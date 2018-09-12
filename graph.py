n, m = map(int, input().split())
A = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    A[u][v] = 1
