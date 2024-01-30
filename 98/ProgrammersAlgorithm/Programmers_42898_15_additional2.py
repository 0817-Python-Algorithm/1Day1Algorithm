def solution(m, n, puddles):
    INF = 1_000_000_007

    dp = [[0] * (m+1) for _ in range(n+1)]
    
    new_puddles = [[j,i] for [i,j] in puddles]

    # 1행 혹은 1열에서 막힌 부분이 있다면 그 밑 부분들은 절대 접근을 할 수 없는 부분들이므로 나머지 뒤에도 싹 다 INF 처리해버려야 함.
    check1 = False
    for i in range(1,m+1):
        if [1,i] in new_puddles:
            check1 = True
        if check1:
            dp[1][i] = INF
        else:
            dp[1][i] = 1

    check2 = False
    for i in range(1,n+1):
        if [i,1] in new_puddles:
            check2 = True
        if check2:
            dp[i][1] = INF
        else:
            dp[i][1] = 1
    
    for [i,j] in new_puddles:
        dp[i][j] = INF

    for i in range(2, n+1):
        for j in range(2, m+1):
            if dp[i][j] < INF:
                # 항상 나머지 나눔이 있으면 중간중간 INF로 나눠줘야 함. 이것이 효율성 테스트에서 좋은 점수를 못받는 이유가 됨.
                if dp[i-1][j] < INF:
                    dp[i][j] += dp[i-1][j] % INF
                if dp[i][j-1] < INF:
                    dp[i][j] += dp[i][j-1] % INF
                dp[i][j] %= INF
    answer = dp[n][m] % INF
    return answer

print(solution(4,3,[[2,2]]))
print(solution(4,3,[[1,2],[2,2]]))
print(solution(1,1,[[1,1]]))