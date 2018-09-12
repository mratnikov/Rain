Color = [0] * (n + 1)
CycleFound = False
def DFS(start):
    Color[start] = 1
    for u in V[start]:
        if Color[u] == 0:
            DFS(u)
        elif Color[start] == 1:
            CycleFound = True
            Color[start] = 2
for i in range(1, n + 1):
    if Color[i] == 0:
        DFS(i)
