def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a > 20 or b > 20 or c>20:
        dp[a][b][c] = w(20,20,20)
        return dp[a][b][c]
    if dp[a][b][c] != None:
        return dp[a][b][c]
    elif a<b and b<c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1, c-1) - w(a,b-1,c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return dp[a][b][c]
dp = [[[None for _ in range(51)] for _ in range(51)] for _ in range(51)]
while(True):
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print('w({}, {}, {}) = {}'.format(a,b,c,w(a,b,c)))
