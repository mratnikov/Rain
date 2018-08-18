def Sum(A):
    if len(A) == 0:
        return 0
    else:
        return Sum(A[:-1]) + A[-1]
