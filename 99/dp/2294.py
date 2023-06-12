N, K = map(int, input().split())
coin = []
for i in range(N):
	coin.append(int(input()))
dp = [0] * (K+1)
dp[0] = 1
coin = sorted(coin,key=lambda x : -x)
for i in range(K+1):
	for j in coin:
		if i-j>=0 and dp[i-j] !=0:
			tmp =  dp[i-j] + dp[j]
			if dp[i] == 0:
				dp[i] = tmp
			else:
				dp[i] = min(dp[i],dp[j]+dp[i-j])
            
if dp[K] == 0:
	print(-1)
else:
    print(dp[K])