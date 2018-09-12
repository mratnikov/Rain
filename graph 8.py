D = [None] * (n + 1)
D[start] = 0
Q = [start]
Qstart = 0
while Qstart < len(Q):
    u = Q[Qstart]
    Qstart += 1
    for v in V[u]:
        if D[v] is None:
            D[v] = D[u] + 1
            Q.append(v)
