import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = sorted(list(map(int, input().rstrip().split())))
result = []
visited = [False] * N

def dfs(index):
    if index == M:
        print(" ".join(map(str, result)))
        return
    else:
        for i in range(0, N):
            if not visited[i]:
                visited[i] = True
                result.append(arr[i])
                dfs(index+1)
                result.pop()
                visited[i] = False

dfs(0)