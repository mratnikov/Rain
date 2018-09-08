Path = []
i = n
while i > 0:
    Path.append(i)
    i = Prev[i]
Path.append(0)
Path = Path[::-1]
