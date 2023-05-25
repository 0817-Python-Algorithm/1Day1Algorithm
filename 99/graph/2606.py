def dfs(num):
    visited[num] = 1
    for next in graph[num]:
        if visited[next] != 1:
            dfs(next)

computer_num = int(input())
network_num = int(input())
graph=[[] for i in range(computer_num+1)]
visited = [0] * (computer_num+1)
for i in range(network_num):
    a,b = map(int, input().split(' '))
    graph[a] += [b]
    graph[b] += [a]
dfs(1)
print(sum(visited)-1)