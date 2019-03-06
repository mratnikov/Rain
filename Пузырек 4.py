N = int(input())
A = []
for k in range(N):
    name,phone = input().split()
    A.append((name,int(phone)))
    for j in range(len(A) - 1, 0, -1):
        for i in range(j):
            if A[i][0] > A[i+ 1][0] \
                    or A[i][0] ==  A[i+ 1][0] and A[i][1] > A[i+ 1][1]:
              A[i], A[i + 1] = A[i+ 1], A[1]
              for k in range (N):
                  name, phone = A[k]

                  print(name, phone)


