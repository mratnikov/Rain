def generate(n, prefix):
    if len(prefix) == n:
        print(prefix)
    else:
        for next in range(1, n + 1):
            if next not in prefix:
                generate(n, prefix + [next])
