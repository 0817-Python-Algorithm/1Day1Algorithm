def solution(arr):
    N = len(arr[0])
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = [arr[0][0], arr[1][0], arr[2][0], arr[0][0] + arr[2][0]]
        
    for i in range(1,N):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + arr[0][i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + arr[1][i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + arr[2][i]
        dp[i][3] = dp[i-1][1] + arr[0][i] + arr[2][i]
    
    return max(dp[N-1])

# 이 문제는 조금 어려웠음.
# 처음엔 이런 방식이 브루트포스 방식이 아닌가 싶단 생각에 점화식을 도출할 생각을 하지 못했음.
# 하지만 arr의 length가 3이라는 제한이 있기에 이 점을 생각하면서 경우들을 따진다면 쉽게 찾을 수 있었을 거란 생각이 듦.

print(solution([[1,3,3,2], [2,1,4,1], [1,5,2,3]]))
print(solution([[1,7,13,2,6], [2,-4,2,5,4], [5,3,5,-3,1]]))