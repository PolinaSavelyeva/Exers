n = int(input())
a = list(map(int, input().split()))
n_sum = n - 2
prefix_sum = [0] * n_sum
prefix_sum[n_sum - 1] = a[n - 1]
for i in reversed(range(0, n_sum - 1)):
    prefix_sum[i] = prefix_sum[i+1] + a[i + 2]

# print(prefix_sum)

for i in range(0, n_sum):
    prefix_sum[i] *= a[i + 1]

# print(prefix_sum)

n_sum_sum = n_sum
prefix_sum_sum = [0] * n_sum_sum
prefix_sum_sum[-1] = prefix_sum[-1]
for i in reversed(range(0, n_sum_sum - 1)):
    prefix_sum_sum[i] = prefix_sum_sum[i + 1] + prefix_sum[i]

# print(prefix_sum_sum)

for i in range(0, n_sum_sum):
    prefix_sum_sum[i] *= a[i]

# print(prefix_sum_sum)

ans = 0
for i in prefix_sum_sum:
    ans += i
print(ans % 1000000007)
