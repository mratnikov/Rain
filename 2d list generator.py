N = 5
M = 5
A =[[i ** j for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        print(A[i][j], end='')
print(A)