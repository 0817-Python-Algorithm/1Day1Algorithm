import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

N, M = map(int, input().rstrip().split(" "))
nodes = [[] for _ in range(N+1)]
visited = [False] * (N+1)

result = 0

def dfs(a):
    global visited
    visited[a] = True
    for node in nodes[a]:
        if not visited[node]:
            dfs(node)
    return

for _ in range(M):
    u, v = map(int, input().rstrip().split(" "))
    nodes[u].append(v)
    nodes[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        result += 1
        dfs(i)
        
print(result)