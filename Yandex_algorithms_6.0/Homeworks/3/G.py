from collections import deque

n, b = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
stack = deque()
for i in range(n):
    stack.append(a[i])
    cur_b = b
    while stack and cur_b:
        popped = stack.popleft()
        if popped <= cur_b:
            ans += (len(stack) + 1) * popped
            cur_b -= popped
        else:
            ans += (len(stack) + 1) * cur_b
            stack.appendleft(popped - cur_b)
            cur_b = 0
while stack:
    popped = stack.popleft()
    ans += (len(stack) + 2) * popped
print(ans)

# for i in range (1):
#     n = randint(1,10)
#     b = randint(1,10)
#     a = sample(range(1, 10), n)
#     f_res = f(n,b,a)
#     native_res = native(n,b,a)
#     if f_res != native_res:
#         print(n,b, a)
#         print(f_res)
#         print(native_res)
#         print()
