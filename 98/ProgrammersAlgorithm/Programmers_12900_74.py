def solution(n):
    
    # 가장 중요한 것은 작은 문제로 쪼개는 능력임.
    # 이 문제의 경우엔 시작을 세로 1개로 두면 나머지는 f(i-1)만큼이고
    # 가로 2개로 두면 나머지는 f(i-2)만큼임.
    # 이런 것을 발견하는 한 끗이 가장 중요함.
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    rem = 1_000_000_007
    for i in range(3, n+1):
        dp[i] = (dp[i-2]%rem + dp[i-1]%rem)%rem
    answer = dp[n]
    return answer

print(solution(4))
print(solution(60000))

