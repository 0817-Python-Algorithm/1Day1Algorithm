def solution(land):
    length = len(land)
    dp = [[0]*4 for i in range(length)]
    dp[0] = land[0]
    
    for i in range(1, length):
        for j in range(4):
            arr = []
            # 윗줄에서 자신과 같은 열이 아닌 애들만 모아서 가장 큰 값이랑 자신이랑 더해줌
            for k in range(4):
                if j != k:
                    arr.append(dp[i-1][k])
            dp[i][j] = max(arr) + land[i][j]
    # 마지막 줄에 최댓값들이 다 모여 있을테니 마지막 줄에서 가장 큰 값을 리턴하면 됨.
    answer = max(dp[length-1])
    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))