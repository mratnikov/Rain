Visited = [False] * (n + 1)
Prev = [None] * (n + 1)
def DFS(start):
    Visited[start] = True
    for u in V[start]:
        if not Visited[u]:
            Prev[u] = start
            DFS(u)
