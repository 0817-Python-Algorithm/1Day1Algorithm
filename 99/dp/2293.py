N, K = map(int, input().split())
coin = []
for i in range(N):
	coin.append(int(input()))
dp = [0] * (K+1)
dp[0] = 1
for i in coin:
	for j in range(i,K+1):
		dp[j] = dp[j] + dp[j-i]

print(dp[K])
