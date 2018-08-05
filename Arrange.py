arr =list(map(int,input().split())) # delaem spisok chisel
n = len(arr)
for i in range(n):
    m = arr[0]
    mi = 0
    for j in range(n - i): # nahodit max
        if arr[j] > m:
            m = arr[j]
            mi = j
    arr[mi], arr[n-1-i] = arr[n-1-i], arr[mi]
    print(*arr)
print(*arr)
