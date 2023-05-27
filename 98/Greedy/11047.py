n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(input())
coins.reverse()
count = 0
for coin in coins:
    count += k//int(coin)
    k %= int(coin)
    if k==0: break
print(count)
