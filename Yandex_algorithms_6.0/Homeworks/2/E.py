n = int(input())
a = sorted(map(int, input().split()))
flag = n % 2 == 0
left = n // 2 - 1
right = left + 1
while left != -1 or right != n:
    if left == -1:
        print(a[right], end=" ")
        right += 1
    elif right == n:
        print(a[left], end=" ")
        left -= 1
    else:
        if flag:
            print(a[left], end=" ")
            left -= 1
        else:
            print(a[right], end=" ")
            right += 1
        flag = not flag
print()
