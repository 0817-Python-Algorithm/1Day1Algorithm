N = int(input())
map = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        dist = map[i][j]
        if i==N-1 and j == N-1:
            print(dp[N-1][N-1])
        if i+dist < N:
            dp[i+dist][j] += dp[i][j]
        if j+dist < N:
            dp[i][j+dist] += dp[i][j]