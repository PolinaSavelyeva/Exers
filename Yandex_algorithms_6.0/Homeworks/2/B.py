N, K = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0] * N
prefix_sum[0] = nums[0]
d = dict()

for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

ans = 0
for i in reversed(range(0, N)):
    d[prefix_sum[i]] = d.get(prefix_sum[i], 0) + 1

    if d.get(prefix_sum[i] + K):
        ans += d[prefix_sum[i]] * d[prefix_sum[i] + K]
    if prefix_sum[i] == K:
        ans += 1
print(ans)
