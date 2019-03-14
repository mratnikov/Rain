def sum(a):
    if len(a) == 0:
        return 0
    else:
        return sum(a[:-1]) + a[-1])
