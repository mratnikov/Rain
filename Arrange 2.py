arr =list(map(int,input().split())) # delaem spisok chisel
n = len(arr)
for i in range(1, n):
    elem = arr[i]
    j = i - 1
    while elem < arr[j] and j >= 0:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = elem
print(*arr)