def generate(n, k, prefix):
    if k == 0:
        print(prefix)
    else:
        if len(prefix) == 0:
            next = 1
        else:
            next = prefix[-1] + 1
        while next + k - 1 <= n:
            generate(n, k - 1, prefix + [next])
            next += 1
