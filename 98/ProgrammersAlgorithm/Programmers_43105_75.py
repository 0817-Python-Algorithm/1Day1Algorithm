def solution(triangle):
    length = len(triangle)
    dp = []
    for i in range(0, length):
        dp.append([0]*(i+1))
    dp[0][0] = triangle[0][0]
    
    for i in range(1, length):
        for j in range(0, i+1):
            # 한 줄에서 맨 왼쪽의 값은 위에서 오른쪽의 값 밖에 못 가져옴.
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            # 한 줄에서 맨 오른쪽의 값은 위에서 왼쪽의 값 밖에 못 가져옴.
            elif i == j:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            # 나머지는 위에서 왼쪽 혹은 오른쪽 중 어떤 값을 가져올지 판단해야 함.
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    answer = max(max(dp))
    return answer

# 미리 그림을 그리고서 접근을 했음.
# 해당 위치까지 오는데 가장 큰 값을 넣어주려고 했음.
# 이때 비교를 해야하는 경우도 있고, 양 끝 위치는 상단에서 오직 한 값으로 밖에 못 받아오는 경우도 있었음.

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))