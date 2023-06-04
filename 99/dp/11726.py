n = int(input())

dp0 = 0
dp1 = 1
dp2 = 0
for i in range(n):
    dp2 = dp0 + dp1
    dp2 = dp2 % 10007
    dp0 = dp1
    dp1 = dp2

print(dp2)
