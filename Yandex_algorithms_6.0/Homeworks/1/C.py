n = int(input())
table = []
for i in range(n):
    str = input()
    row = []
    for j in range(n):
        row.append(str[j])
    table.append(row)

# for i in range (n):
#     for j in range (n):
#         print(table[i][j], end=" ")
#     print(f"\n", end="")

minimal_I = [
    ["#"]
]

minimal_O = [
    ["#", "#", "#"],
    ["#", ".", "#"],
    ["#", "#", "#"]
]

minimal_C = [
    ["#", "#"],
    ["#", "."],
    ["#", "#"]
]

minimal_L = [
    ["#", "."],
    ["#", "#"]
]

minimal_H = [
    ["#", ".", "#"],
    ["#", "#", "#"],
    ["#", ".", "#"]
]

minimal_P = [
    ["#", "#", "#"],
    ["#", ".", "#"],
    ["#", "#", "#"],
    ["#", ".", "."]
]


def find_letter(n, table):

    compressed_rows = []
    i = 0
    while i < n:
        while i < n - 1 and table[i] == table[i+1]:
            i += 1
        compressed_rows.append(table[i])
        i += 1

    transpose_compressed_rows = []
    for j in range(len(compressed_rows[0])):
        row = []
        for i in range(len(compressed_rows)):
            row.append(compressed_rows[i][j])
        transpose_compressed_rows.append(row)

    compressed_columns = []
    i = 0
    while i < n:
        while i < n - 1 and transpose_compressed_rows[i] == transpose_compressed_rows[i+1]:
            i += 1
        compressed_columns.append(transpose_compressed_rows[i])
        i += 1

    transpose_compressed_columns = []
    for j in range(len(compressed_columns[0])):
        row = []
        for i in range(len(compressed_columns)):
            row.append(compressed_columns[i][j])
        transpose_compressed_columns.append(row)

    rows = len(transpose_compressed_columns)
    columns = len(transpose_compressed_columns[0])

    # for i in range (rows):
    #     for j in range (columns):
    #         print(transpose_compressed_columns[i][j], end=" ")
    #     print(f"\n", end="")

    upper, left = 0, 0
    lower, right = rows - 1, columns - 1

    # print(rows, columns)

    if transpose_compressed_columns[0] == ["."] * columns:
        upper = 1
    if transpose_compressed_columns[rows - 1] == ["."] * columns:
        lower = rows - 2
    if compressed_columns[0] == ["."] * rows:
        left = 1
    if compressed_columns[columns - 1] == ["."] * rows:
        right = columns - 2

    # print(f"upper: {upper}", f"lower: {lower}", f"left: {left}", f"right: {right}")

    match lower - upper + 1:
        case 4:
            if right - left + 1 == 3:
                for i in range(upper, lower + 1):
                    for j in range(left, right + 1):
                        if minimal_P[i - upper][j - left] != transpose_compressed_columns[i][j]:
                            return ("X")
                return ("P")
            else:
                return ("X")
        case 3:
            if right - left + 1 == 3:
                for i in range(upper, lower + 1):
                    for j in range(left, right + 1):
                        if minimal_H[i - upper][j - left] != transpose_compressed_columns[i][j]:
                            for i in range(upper, lower + 1):
                                for j in range(left, right + 1):
                                    if minimal_O[i - upper][j - left] != transpose_compressed_columns[i][j]:
                                        return ("X")
                            return ("O")
                return ("H")
            elif right - left + 1 == 2:
                for i in range(upper, lower + 1):
                    for j in range(left, right + 1):
                        if minimal_C[i - upper][j - left] != transpose_compressed_columns[i][j]:
                            return ("X")
                return ("C")
            else:
                return ("X")
        case 2:
            if right - left + 1 == 2:
                for i in range(upper, lower + 1):
                    for j in range(left, right + 1):
                        if minimal_L[i - upper][j - left] != transpose_compressed_columns[i][j]:
                            return ("X")
                return ("L")
            else:
                return ("X")
        case 1:
            if right - left + 1 == 1:
                return ("I")
            else:
                return ("X")
        case _:
            return ("X")

    # for i in range (len(transpose_compressed_columns)):
    #     for j in range (len(transpose_compressed_columns[0])):
    #         print(transpose_compressed_columns[i][j], end=" ")
    #     print(f"\n", end="")


print(find_letter(n, table))

# table = [
#     ['#', '#', '.', '#', '.'],
#     ['#', '#', '.', '#', '.'],
#     ['#', '#', '#', '#', '.'],
#     ['#', '#', '.', '#', '.'],
#     ['#', '#', '.', '#', '.']
# ]
# print(find_letter(5, table)=="H")

# table = [
#     ['.', '#', '#', '#', '.'],
#     ['.', '#', '.', '#', '.'],
#     ['.', '#', '#', '#', '.'],
#     ['.', '#', '.', '.', '.'],
#     ['.', '#', '.', '.', '.']
# ]
# print(find_letter(5, table)=="P")

# table = [
#     ['#', '#', '#', '#', '#'],
#     ['#', '#', '#', '#', '#'],
#     ['#', '#', '#', '#', '#'],
#     ['#', '#', '#', '.', '#'],
#     ['#', '#', '#', '#', '#']
# ]
# print(find_letter(5, table)=="O")

# table = [
#     ['.', '#', '#', '#', '.'],
#     ['.', '#', '#', '#', '.'],
#     ['.', '#', '#', '.', '.'],
#     ['.', '#', '#', '.', '.'],
#     ['.', '#', '#', '#', '.']
# ]
# print(find_letter(5, table)=="C")


# table = [
#     ['.', '.', '.', '.', '.'],
#     ['.', '#', '#', '.', '.'],
#     ['.', '#', '#', '.', '.'],
#     ['.', '#', '#', '.', '.'],
#     ['.', '#', '#','.', '.']
# ]
# print(find_letter(5, table)=="I")

# table = [
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '#', '.','.', '.']
# ]
# print(find_letter(5, table)=="I")

# table = [
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', '#', '.', '.'],
#     ['.', '#', '.','.', '.']
# ]
# print(find_letter(5, table)=="X")
