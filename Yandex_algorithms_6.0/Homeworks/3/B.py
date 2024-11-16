from collections import deque


N = int(input())
costs = list(map(int, input().split()))
stack = deque()
nearest_cheapest = [-1] * N
for i in range(N):
    while len(stack):
        popped_cost, popped_index = stack.pop()
        if popped_cost > costs[i]:
            nearest_cheapest[popped_index] = i
        else:
            stack.append([popped_cost, popped_index])
            break
    stack.append([costs[i], i])
print(*nearest_cheapest, sep=" ")
