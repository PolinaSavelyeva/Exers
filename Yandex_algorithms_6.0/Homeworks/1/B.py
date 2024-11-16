A, B, C, D = [int(input()) for i in range(4)]

if A == 0:
    print(1, C + 1)
elif C == 0:
    print(A + 1, 1)
elif B == 0:
    print(1, D + 1)
elif D == 0:
    print(B + 1, 1)
elif B + D <= A + C:
    if max(A, B) <= B + D:
        if max(C, D) <= B + D and max(C, D) <= max(A, B):
            if C > D:
                print(1, C + 1)
            else:
                print(1, D + 1)
        else:
            if A > B:
                print(A + 1, 1)
            else:
                print(B + 1, 1)
    elif max(C, D) <= B + D:
        if C > D:
            print(1, C + 1)
        else:
            print(1, D + 1)
    else:
        print(B + 1, D + 1)
else:
    if max(A, B) <= A + C:
        if max(C, D) <= B + D and max(C, D) <= max(A, B):
            if C > D:
                print(1, C + 1)
            else:
                print(1, D + 1)
        else:
            if A > B:
                print(A + 1, 1)
            else:
                print(B + 1, 1)
    elif max(C, D) <= A + C:
        if C > D:
            print(1, C + 1)
        else:
            print(1, D + 1)
    else:
        print(A + 1, C + 1)

# 790
# 493
# 507
# 302

# from random import randint

# def f(A, B, C, D):
#     M = min(A + 1, B + 1)
#     N = min(C + 1, D + 1)
#     return M, N


# A = 1
# B, C, D = [randint(0,10**3) for i in range (3)]
# print(A, B, C, D)
# print(f(A, B, C, D))
# print(A + C)
# print(B + D)

# 1 307 841 524
# (308, 525)
# 842
# 831


# if f(6, 2, 7, 3) == (3, 4):
#     print("Success 1")

# if f(10**9, 10**9, 10**9, 10**9) == (10**9 + 1, 10**9 + 1):
#     print("Success 2")

# if f(0, 5, 1, 2) == (1, 2):
#     print("Success 3")

# if f(7, 2, 9, 3) == (3, 4):
#     print("Success 4")

# if f(100, 100, 100, 0) == (101, 1):
#     print("Success 5")

# if f(1, 115, 0, 100) == (2, 1):
#     print("Success 6")

# if f(200, 0, 300, 100) == (1, 101):
#     print("Success 7")

# if f(200, 0, 300, 0) == (1, 1):
#     print("Success 8")

# if f(0, 1371, 0, 13910) == (1, 1):
#     print("Success 9")
