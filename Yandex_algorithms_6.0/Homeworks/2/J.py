n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x = list(map(int, input().split()))
asc_indexes = []
prev = a[0]
for i in range(1, n):
    if prev > a[i]:
        asc_indexes.append(i-1)
    prev = a[i]
asc_indexes.append(n-1)
prefix_sum = [0] * n
prefix_sum[0] = 0
# префиксная сумма с пятого до 0-ого элемента имеет к одинаковых перходов
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + (a[i] == a[i-1])
# макимальный индекс к которому можно прийти начиная с индекса i
max_index = [0] * n
p = n - 1
for i in reversed(range(n)):
    while p >= 0 and prefix_sum[i] - prefix_sum[p] <= k:
        p -= 1
    p += 1
    max_index[i] = p
if len(asc_indexes) > 1:
    for i in range(1, len(asc_indexes)):
        left = asc_indexes[i-1] + 1
        right = asc_indexes[i] + 1
        for j in range(left, right):
            if max_index[j] < left:
                max_index[j] = left
for i in x:
    print(max_index[i-1] + 1, end=" ")
print()
