def BubleSort (A):
    for j in range (len(A) - 1, 0, -1):
        for i in range(0, j):
            if A[i][0] > A[i+ 1][0]: #сравниваем не кортежи а ключи
                A[i], A[i+ 1] = A[i+ 1], A[i]
A = [(4,'Milena'),(2,'Oleksa'),(3,'Andrey'),(5,'Andrey')]

BubleSort(A)
print(BubleSort(A))