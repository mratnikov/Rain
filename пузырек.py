def BubleSort(A):
    for j in range(len(A)):
        for i in range(len(A)):
            if A[i] > A[i+1]:
                A[i], A[i + 1] = A[i + 1], A[i]
