length = list(map(int, input().split()))
left = 0
right = len(length) - 1
max_area = 0

while left < right:
    area = (min(length[left], length[right])) * (right - left)
    max_area = max(max_area, area)
    if length[left] < length[right]:
        left += 1
    else:
        right -= 1

print(max_area)