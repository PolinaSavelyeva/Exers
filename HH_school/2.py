from collections import deque, defaultdict


def bfs(graph):

    map = defaultdict(list)
    for i, continent in enumerate(graph):
        map[continent].append(i)

    queue = deque([0])
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    steps = 0
    max_continent = max(graph)
    min_continent = min(graph)
    visited_islands = [False] * (max_continent - min_continent + 1)

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()

            if current == n - 1:
                return steps

            if not visited[current + 1]:
                visited[current + 1] = True
                queue.append(current + 1)

            if current != 0 and not visited[current - 1]:
                visited[current - 1] = True
                queue.append(current - 1)

            if not visited_islands[graph[current] - min_continent]:
                visited_islands[graph[current] - min_continent] = True
                for neighbor in map[graph[current]]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        steps += 1


islands = list(map(int, input().split()))
print(bfs(islands))