Visited = [False] * (n + 1)
Ans = []
def DFS(start):
    Visited[start] = True
    for u in V[start]:
        if not Visited[u]:
            DFS(u)
    Ans.append(start)

for i in range(1, n + 1):
    if not Visited(i):
        DFS(i)
Ans = Ans[::-1]
