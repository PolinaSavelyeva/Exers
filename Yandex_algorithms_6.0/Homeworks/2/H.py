# from random import randint, sample
# 5 2 3 1
# space_0 = 5 * 0 + 2 * 1 + 3 * 2 + 1 * 3 = 11
# space_1 = 5 * 1 + 2 * 0 + 3 * 1 + 1 * 2 = space_0 + 5 - 2 - 3 - 1 = 10
# space_2 = 5 * 2 + 2 * 1 + 3 * 0 + 1 * 1 = space_1 + 5 + 2 - 3 - 1 =
# space_3 = 5 * 3 + 2 * 2 + 3 * 1 + 1 * 0 = space_2 + 5 + 2 + 3 - 1

n = int(input())
a = list(map(int, input().split()))


def f(n, a):
    space = 0
    for i in range(1, n):
        space += i * a[i]
    ans = space
    sums = [0] * n
    sums[0] = a[0]
    for i in range(1, n):
        sums[0] -= a[i]
    for i in range(1, n):
        sums[i] = sums[i-1] + 2 * a[i]
    for i in range(1, n):
        space = space + sums[i-1]
        ans = min(ans, space)
    return (ans)


def native(n, a):
    ans = 0
    for space in range(n):
        ans += a[space] * space

    for open_space in range(n):
        p = 0
        for space in range(n):
            p += a[space] * abs(open_space - space)
        ans = min(ans, p)
    return ans


print(f(n, a))
# print(f(4,[5,2,3,1])==10)
# print(f(5,[5,4,3,2,1])==15)
# for i in range (1):
#     n = randint(1,2*10**5)
#     a = sample(range(1, 10**9), n)>
#     f_res = f(n,a)
#     native_res = native(n,a)
#     if f_res != native_res:
#         print(n,a)
#         print(f_res)
#         print(native_res)
#         print()
