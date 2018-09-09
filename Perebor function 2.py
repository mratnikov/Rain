def generate(n, prefix):
    if n == 0:
        print(prefix)
    else:
        generate(n - 1, prefix + "0")
        if prefix == "" or prefix[-1] == "0":
            generate(n - 1, prefix + "1")
