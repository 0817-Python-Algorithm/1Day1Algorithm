def solution(land):
    length = len(land)
    dp = [[0]*4 for i in range(length)]
    dp[0] = land[0]
    
    for i in range(1, length):
        for j in range(4):
            # 윗줄에서 자신과 같은 열이 아닌 애들만 모아서 가장 큰 값이랑 자신이랑 더해줌.
            # 팁: 이런 방식으로 j번째꺼만 빼고 모을 수 있음. 정말 좋은 스킬
            arr = dp[i-1][0:j] + dp[i-1][j+1:]
            dp[i][j] = max(arr) + land[i][j]
    # 마지막 줄에 최댓값들이 다 모여 있을테니 마지막 줄에서 가장 큰 값을 리턴하면 됨.
    answer = max(dp[length-1])
    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))