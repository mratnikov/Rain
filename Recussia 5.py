def Max(A):
    if len(A) == 1:
        return A[0]
    else:
        return max(Max(A[:-1]), A[-1])
