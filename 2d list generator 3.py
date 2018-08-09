N = 5
M = 5
A =[[i ** j for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        if i < j:
            A[i][j] = "ln"
        elif i == j:
            A[i][j] = "d"
        else:
            A[i][j] = "vp"