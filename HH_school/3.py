# Самостоятельная задача:
# Дана матрица и вводной слово, нужно выяснить существует ли это слово в матрице, если перемещаться по клеткам по горизонтали и вертикали:
# 
from collections import deque, defaultdict


def find_word(word_to_find, matrix, rows, columns, current_i, current_j):

    if not word_to_find:
        return True
    if current_i != 0 and word_to_find[0] == matrix[current_i - 1][current_j]:
        return find_word(word_to_find[1:], matrix, rows, columns,current_i - 1, current_j)
    if current_i != rows - 1 and word_to_find[0] == matrix[current_i + 1][current_j]:
        return find_word(word_to_find[1:], matrix, rows, columns, current_i + 1, current_j)
    if current_j != 0 and word_to_find[0] == matrix[current_i][current_j - 1]:
        return find_word(word_to_find[1:], matrix, rows, columns, current_i, current_j - 1)
    if current_j != columns - 1 and word_to_find[0] == matrix[current_i][current_j + 1]:
        return find_word(word_to_find[1:], matrix, rows, columns, current_i, current_j + 1)
    return False

def f(matrix, rows, columns, word):
    for i in range (rows):
        for j in range (columns):
            if matrix[i][j] == word[0] and find_word(word[1:], matrix, rows, columns, i, j):
                    return True
    return False

rows = int(input("Enter the number of rows:"))
# columns = int(input("Enter the number of columns:"))
# word = input()
matrix = []
for i in range (rows):
    matrix.append(list(map(int, input().split())))

# matrix = [[input() for x in range (columns)] for y in range(rows)]  

# # print(word)
# # print(matrix)
# print(f(matrix, rows, columns, word))

matrix = [
    ['A', 'F', 'R', 'D', 'H'],
    ['O', 'L', 'M', 'O', 'E'],
    ['L', 'M', 'Q', 'L', 'L']
]
word = 'HELLO'

if f(matrix, len(matrix), len(matrix[0]), word):
    print("success")

matrix = [
    ['A', 'F', 'R', 'D', 'H'],
    ['O', 'L', 'M', 'O', '*'],
    ['L', 'M', 'Q', 'L', 'L']
]

if not f(matrix, len(matrix), len(matrix[0]), word):
    print("success")

matrix = [
    ['O', 'A']
]
word = 'OAOA'

if f(matrix, len(matrix), len(matrix[0]), word):
    print("success")