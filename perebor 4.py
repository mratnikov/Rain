def generate(n, k, prefix):
    if n == 0:
        print(prefix)
    else:
        if k < n:
            generate(n - 1, k, prefix + "0")
        if k > 0:
            generate(n - 1, k - 1, prefix + "1")
