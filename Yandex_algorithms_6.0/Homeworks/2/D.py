n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
right = 0
a = sorted(a)
for left in range(n):
    while right < n and abs(a[left] - a[right]) <= k:
        right += 1
    if right == n:
        ans += n - left
        break
    right += 1
print(ans)
