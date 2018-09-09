A = list(map(int, input().split()))
min_diff = abs(A[1]-A[0]) + 1
for k in range(1, len(A)):
    for i in range(k):
        if abs(A[k] - A[i]) < min_diff:
            min_diff = abs(A[k] - A[i])
            x = A[i]
            y = A[k]
print(x, y)
