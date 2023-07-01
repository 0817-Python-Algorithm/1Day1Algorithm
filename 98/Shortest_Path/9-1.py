import sys

input = sys.stdin.readline

infinite = int(1e9)

n, m = map(int, input().split())
start = int(input())

edges = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [infinite] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])


def get_smallest_node():
    min_value = infinite
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(initial):
    distance[initial] = 0
    visited[initial] = True
    for i in edges[initial]:
        distance[i[0]] = i[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in edges[now]:
            cost = j[1] + distance[now]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1, 1):
    if distance[i] == infinite:
        print("INFINITY")
    else:
        print(distance[i])
