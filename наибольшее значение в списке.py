def max(a):
    if len(a) == 1
        return a[0]
    else:
        return max(max(a[:-1]), a[:1])