s = int(input())
arr = list(map(int,input().split()))
d = abs (s -(arr[0] % 10) + ((arr[0] // 10) % 10) + (arr[0] // 100))
ans = arr[0]
for elem in arr:
    if abs(s -((elem % 10) + ((elem // 10) % 10) + (elem // 100))) < d:
        d = (s -((elem % 10) + ((elem // 10) % 10) + (elem // 100)))
        ans = elem
print (ans)