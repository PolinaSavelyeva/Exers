# from random import randint, choice

n, c = map(int, input().split())
t = input()


def f(n, c, t):
    l = r = best_l = best_r = c_cur = b_cur = a_cur = 0
    while r < n:
        match t[r]:
            case 'a':
                a_cur += 1
            case 'b':
                b_cur += 1
                c_cur += a_cur
        if c_cur <= c:
            if r - l > best_r - best_l:
                best_r, best_l = r, l
            r += 1
        else:
            while l < n and c_cur > c:
                match t[l]:
                    case 'a':
                        a_cur -= 1
                        c_cur -= b_cur
                    case 'b':
                        b_cur -= 1
                l += 1
            if r - l > best_r - best_l:
                best_r, best_l = r, l
            r += 1
    return (best_r - best_l + 1)


print(f(n, c, t))

# def native(n,c,t):
#     ans = 0
#     for i in range (n):
#         for j in range (n):
#             a_count=c_count=0
#             for k in range (i, j+1):
#                 if t[k] == 'a':
#                     a_count += 1
#                 elif t[k] == 'b':
#                     c_count += a_count
#             if c_count <= c:
#                 ans = max(ans, j - i + 1)
#     return(ans)

# for i in range (1000):
#     n, c = randint(1,20), randint(0,50)
#     t = [0] * n
#     smpl = ['a','b','c']
#     for i in range (n):
#         t[i] = choice(smpl)
#     if f(n,c,t)!=native(n,c,t):
#         print(n,c,t)
#         print(f(n,c,t))
#         print(native(n,c,t))
#         print()
# n = 50
# c = 159
# t = 'aaabaababaabaaaabaabbxaazbaaaababaababbbaaaabaabbb'
# print(n,c,t)
# print(f(n,c,t))
# print(native(n,c,t))
# print()
