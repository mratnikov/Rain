Visited = [False] * (n + 1)
def DFS(start):
    Visited[start] = True
    for v in V[start]:
        if not Visited[v]:
            DFS(v)

NComp = 0
for i in range(1, n + 1):
    if not Visited(i):
        NComp += 1
        DFS(i)
