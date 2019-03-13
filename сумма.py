def summ (n):
    if n == 0:
        return 1
    else:
        return n + summ (n -1)