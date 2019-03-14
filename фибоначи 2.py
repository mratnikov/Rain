def Feb(n):
    if n <= 1:
        return
    else:
        return Feb(n-1) + Feb(n - 2)
