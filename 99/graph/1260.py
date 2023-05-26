def dfs(V):
    print(V, end=' ')
    isVisited[V] = 1
    for i in edge[V]:
        if isVisited[i] == 0:
            dfs(i)

def bfs(V):
    q = []
    q.append(V)
    isVisited[V] = 1
    while(len(q) !=0):
        item = q.pop(0)
        print(item, end=' ')
        for i in edge[item]:
            if isVisited[i] == 0:
                q.append(i)
                isVisited[i] = 1

N, M, V = map(int, input().split())
edge = [[] for i in range(N+1)]
isVisited = [0] * (N+1)
for i in range(M):
    a,b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
for i in range(N+1):
    edge[i] = sorted(edge[i])
dfs(V)
isVisited = [0] * (N+1)
print()
bfs(V)