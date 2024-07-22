import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [i for i in range(1, N+1)]
visited = [False] * N
results = [0] *M

def dfs(index):
    global visited
    global results
    global M

    if index == M:
        print(" ".join(map(str, results)))
        return
    else:
        for i in range(0,N):
            if not visited[i]:
                visited[i] = True
                results[index] = i+1
                dfs(index+1)
                visited[i] = False
            else:
                continue

dfs(0)