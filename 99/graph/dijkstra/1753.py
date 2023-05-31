import heapq
import sys
input = sys.stdin.readline
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    answer[start] = 0
    while(q):
        (d,v) = heapq.heappop(q)
        if answer[v] < d:
            continue
        for v_next, w_next in edge[v]:
            if answer[v_next] > d + w_next:
                heapq.heappush(q, ((d+w_next), v_next))
                answer[v_next] = d + w_next

V, E = map(int, input().split())
start = int(input())
edge = [[] for _ in range(V+1)]
answer = [float('INF') for _ in range(V+1)]
for i in range(E):
    a,b,w = map(int, input().split())
    edge[a].append((b,w))
dijkstra(start)
for a in answer[1:]:
    if a == float('inf'):
        print('INF')
    else:
        print(a)