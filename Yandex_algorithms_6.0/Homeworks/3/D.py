from collections import deque


str = list(input().split())
stack = deque()
for char in str:
    if char.isdigit():
        stack.append(char)
    elif char == '*':
        stack.append(int(stack.pop()) * int(stack.pop()))
    elif char == '+':
        stack.append(int(stack.pop()) + int(stack.pop()))
    elif char == '-':
        snd = int(stack.pop())
        fst = int(stack.pop())
        stack.append(fst - snd)
print(int(stack.pop()))
