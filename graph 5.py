Color = [0] * (n + 1)
IsBipartite = True
def DFS(start):
    for u in V[start]:
        if Color[u] == 0:
            Color[u] = 3 - Color[start]
            DFS(u)
        else if Color[u] == Color[start]:
            IsBipartite = False

for i in range(1, n + 1):
    if Color[i] == 0:
        Color[i] = 1 DFS(i)
