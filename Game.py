n = int(input())
k = int(input())

ans = [0] * (n + 1)
for i in range (1, k + 1):
    ans[i] = 1

for i in range (n + 1, k + 1):
    flag = False
    for j in range (1, k + 1):
        if (ans[i - j] == 2) and ((i-j) % 3 !=0):
            flag = True
        if flag:
            ans[i] = 1
        else:
            ans[i] = 2

print (ans[n])