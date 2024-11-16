from collections import deque


n, k = list(map(int, input().split()))
seq = list(map(int, input().split()))
deq = deque()
for i in range(k):
    while len(deq):
        popped_right = deq.pop()
        if popped_right <= seq[i]:
            deq.append(popped_right)
            break
    deq.append(seq[i])
popped_left = deq.popleft()
print(popped_left)
if seq[0] != popped_left:
    deq.appendleft(popped_left)

for i in range(k, n):
    while len(deq):
        popped_right = deq.pop()
        if popped_right <= seq[i]:
            deq.append(popped_right)
            break
    deq.append(seq[i])
    popped_left = deq.popleft()
    print(popped_left)
    if seq[i+1-k] != popped_left:
        deq.appendleft(popped_left)
