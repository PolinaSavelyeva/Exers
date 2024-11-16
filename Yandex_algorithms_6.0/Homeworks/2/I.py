n = int(input())
interest = list(map(int, input().split()))
helpful = list(map(int, input().split()))
mood = list(map(int, input().split()))


def f(n, interest, helpful, mood):
    def sort_by_indexes(n, fst_list, snd_list):
        tmp = [[0, 0, 0]] * n
        for i in range(n):
            tmp[i] = [i, fst_list[i], snd_list[i]]
        tmp.sort(key=lambda a: (a[1], a[2], i), reverse=True)
        return tmp

    sorted_interest = sort_by_indexes(n, interest, helpful)
    sorted_helpful = sort_by_indexes(n, helpful, interest)
    chosen_indexes = [False] * n

    # ans = []

    p_interest = p_helpful = 0
    for i in mood:
        if i:
            while chosen_indexes[sorted_helpful[p_helpful][0]]:
                p_helpful += 1
            print(sorted_helpful[p_helpful][0] + 1, end=" ")
            # ans.append(sorted_helpful[p_helpful][0] + 1)
            chosen_indexes[sorted_helpful[p_helpful][0]] = True
        else:
            while chosen_indexes[sorted_interest[p_interest][0]]:
                p_interest += 1
            print(sorted_interest[p_interest][0] + 1, end=" ")
            # ans.append(sorted_interest[p_interest][0] + 1)
            chosen_indexes[sorted_interest[p_interest][0]] = True
    print()


    # return ans
f(n, interest, helpful, mood)
# import heapq
# from random import sample, randint, choice

# def native(n, a, b, p):
#     # Инициализация двух куч и множества для отслеживания изученных алгоритмов
#     heap_a = []
#     heap_b = []
#     studied = set()

#     # Наполнение куч начальными значениями
#     for i in range(n):
#         heapq.heappush(heap_a, (-a[i], -b[i], i))
#         heapq.heappush(heap_b, (-b[i], -a[i], i))

#     result = []

#     # Обработка дней
#     for day in range(n):
#         if p[day] == 1:
#             # Вася воодушевлен, выбирает алгоритм с максимальной полезностью
#             while heap_b:
#                 _, _, i = heapq.heappop(heap_b)
#                 if i not in studied:
#                     studied.add(i)
#                     result.append(i + 1)
#                     break
#         else:
#             # Вася скучает, выбирает алгоритм с максимальной интересностью
#             while heap_a:
#                 _, _, i = heapq.heappop(heap_a)
#                 if i not in studied:
#                     studied.add(i)
#                     result.append(i + 1)
#                     break

#     return result

# for i in range (10000):
#     n = randint(1,3)
#     interest = sample(range(1, 4), n)
#     helpful = sample(range(1, 4), n)

#     mood = [0]*n
#     consts = [0,1]
#     for i in range (n):
#         mood[i]=choice(consts)
#     f_res = f(n,interest, helpful, mood)
#     native_res = native(n,interest, helpful, mood)
#     if f_res != native_res:
#         print(n, interest, helpful, mood)
#         print(f_res)
#         print(native_res)
#         print()

# 10 [111, 40, 112, 65, 158, 16, 144, 79, 29, 91] [93, 3, 55, 63, 91, 90, 40, 172, 85, 108]
# [8, 10, 1, 5, 6, 9, 4, 3, 7, 2]
# [5, 7, 3, 1, 10, 8, 4, 2, 9, 6]

# 5
#   0    1  2   3    4
# [139, 24, 69, 27, 63]
# [47, 173, 181, 165, 56]
# [1, 1, 1, 1, 1]

# [3, 2, 4, 5, 1]
# [1, 3, 5, 4, 2]
