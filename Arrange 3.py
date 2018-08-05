arr =list(map(int,input().split())) # delaem spisok chisel
n = len(arr)
cnt = [0] * 10

for i in range( n):
    cnt[arr[i]] += 1

ans = []
for i in range(len(cnt)):
    ans = ans + ([i] * cnt[i])

print(*ans)