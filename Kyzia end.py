Path = []
i = n
while i > 0:
    if C[i — 1] < C[i — 2]:
        prev = i — 1
    else:
        prev = i - 2
    Path.append(prev)
    i = prev
Path.append(0)
Path = Path[::-1]
