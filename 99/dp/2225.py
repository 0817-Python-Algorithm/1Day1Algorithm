N,K = map(int,input().split())
dp = [1] * (K+1)
for i in range(N):
    for j in range(2,K+1):
        dp[j] = (dp[j] +dp[j-1])%1000000000
print(dp[K])