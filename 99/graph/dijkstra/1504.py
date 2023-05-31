import sys
import copy
import heapq
input = sys.stdin.readline
def dijkstra(start):
    dir = [float('inf') for _ in range(N+1)]
    q = []
    heapq.heappush(q,(0,start))
    dir[start] = 0
    while(q):
        (curr_w, curr_pos) = heapq.heappop(q)
        # if dir[start][curr_pos] < curr_pos:
        #     continue
        for next_w, next_pos in graph[curr_pos]:
            if curr_w + next_w < dir[next_pos]:
                dir[next_pos] = curr_w + next_w
                heapq.heappush(q,(next_w+curr_w, next_pos))
    return dir

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a,b,w = map(int, input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))
p1, p2 = map(int, input().split())
d1=  dijkstra(1)
d2 = dijkstra(p1)
d3 = dijkstra(p2)
a1 = d1[p1] + d2[p2] + d3[N]
a2 = d1[p2] + d3[p1] + d2[N]
answer = min(a1,a2)
if answer >= float('inf'):
    print(-1)
else:
    print(answer)