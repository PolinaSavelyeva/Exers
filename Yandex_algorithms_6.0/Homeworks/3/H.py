from collections import deque


n = int(input())
stack = deque()
prefix_sum = [0]
ans = []
for i in range(n):
    oper = input()
    sign = oper[0]
    if sign == '+':
        elem = int(oper[1:])
        stack.append(elem)
        prefix_sum.append(elem + prefix_sum[-1])
    elif sign == '-' or sign == '−':
        ans.append(stack.pop())
        prefix_sum.pop()
    elif sign == '?':
        k = int(oper[1:])
        ans.append(prefix_sum[-1] - prefix_sum[-k - 1])
print(*ans, sep="\n")
