def BubleSort (A,B):
    for j in range (len(A) - 1, 0, -1):
        for i in range(0, 1):
            if A[i] > A[i+ 1]:
                A[i], A[i+ 1] = A[i+ 1], A[i]
                B[i], B[i+ 1] = B[i+ 1], B[i]

A = [4,2,5,1]
B = ['Ivan', 'Milena','Oleg','Ira']

BubleSort(A,B)

print(A,B ,BubleSort(A,B))