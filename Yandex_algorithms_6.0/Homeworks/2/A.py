n = int(input())
nums = map(int, input().split())
prefix_sum = 0
for num in nums:
    prefix_sum += num
    print(prefix_sum, end=" ")
print()
