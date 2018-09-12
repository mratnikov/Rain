n, m = map(int, input().split())
W = [set() for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    W[u].add(v)
