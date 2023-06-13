import queue
M, N = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(M)]
dir = [(-1,0),(1,0),(0,1),(0,-1)]
dp = [[-1] * N for _ in range(M)]
def dfs(y,x):
    if y==M-1 and x ==N-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    count = 0
    for d in dir:
        nextX = x + d[0]
        nextY = y + d[1]
        if 0<=nextX<N and 0<=nextY<M:
            if map[nextY][nextX] < map[y][x]:
                count += dfs(nextY, nextX)
    dp[y][x] = count
    return dp[y][x]
print(dfs(0,0))