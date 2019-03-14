def number(a,n):
    if n == 0:
        return 1
    elif n %2 == 1:
        return number(a, n -1) * a
    else:
        return number (a, n//2) ** 2