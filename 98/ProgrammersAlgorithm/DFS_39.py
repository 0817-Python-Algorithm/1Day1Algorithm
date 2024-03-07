from collections import defaultdict, deque


def solution(graph, start):

    result = []
    visited = set()
    q = deque()
    linked_list = defaultdict(list)

    for a, b in graph:
        linked_list[a].append(b)

    def dfs(start, result, q, visited):

        if start in visited:
            return
        visited.add(start)
        result.append(start)

        for l in linked_list[start]:
            if l not in visited:
                q.append(l)
    q.append(start)
    while q:
        dfs(q.popleft(), result, q, visited)
    return result


print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8),
      (5, 8), (6, 9), (7, 9)], 1))  # 반환값 :[1, 2, 3, 4, 5, 6, 7, 8, 9]
# 반환값 : [1, 2, 3, 4, 5, 0]
print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1))
