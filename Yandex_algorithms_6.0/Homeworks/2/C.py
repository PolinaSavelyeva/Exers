n, r = map(int, input().split())
d = list(map(int, input().split()))
right = ans = 0
for left in range(n):
    while right < n and d[right] - d[left] <= r:
        right += 1
    ans += n - right

print(ans)
