N = int(input())
dp0 = 1
dp1 = 0
dp2 = 0
for i in range(N):
    dp2 = dp0 + dp1
    dp0 = dp1
    dp1 = dp2
print(dp2)
