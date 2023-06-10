from collections import deque
subin, yong = map(int, input().split())
dist = [float('inf') for _ in range(100001)]
def bfs():
    q = deque()
    q.append(subin)
    dist[subin] = 0
    while(q):
        curr = q.popleft()
        if curr < yong:
            if curr*2 < 100001 and dist[curr*2] > dist[curr]:
                q.append(curr*2)
                dist[curr*2] = dist[curr]
            if curr+1 < 100001 and dist[curr+1] > dist[curr]+1:        
                q.append(curr+1)
                dist[curr+1] = dist[curr]+1
        if curr -1 >= 0 and dist[curr-1] > dist[curr]+1:
            q.append(curr-1)
            dist[curr-1] = dist[curr]+1
bfs()
print(dist[yong])