from collections import deque


def f():
    brackets_dict = {'(': ')', '[': ']'}
    n = int(input())
    w = input()
    w_dict = dict()
    for i in range(len(w)):
        w_dict[w[i]] = i
    s = input()
    n -= len(s)
    stack = deque()
    for i in s:
        if i == ')' or i == ']':
            stack.pop()
        else:
            stack.append(i)
    # количество пар скобок, которое можно добавить
    pairs_count = (n - len(stack)) // 2
    # и у нас два пути в зависимости от весов w
    # сначала последовательность открытых скобок затем закрытых
    # открытые скобки чередуются с закрытыми
    # а перед эти нужно решить, когда закрыть скобки в стеке
    while pairs_count:
        if stack:
            popped = stack.pop()
            # закрываем существующую если нам невыгодно открыть никакую новую
            if w_dict[brackets_dict[popped]] < w_dict['(']:
                if w_dict[brackets_dict[popped]] < w_dict['[']:
                    s += brackets_dict[popped]
                    continue
            stack.append(popped)
        pairs_count -= 1
        if w_dict['('] < w_dict['[']:
            s += '('
            stack.append('(')
        else:
            s += '['
            stack.append('[')
    while stack:
        s += brackets_dict[stack.pop()]
    return s


print(f())
