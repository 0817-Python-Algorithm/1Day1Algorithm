def solution(nums):

    N = len(nums)
    dp = [0] * N
    
    dp[0] = 1
    for i in range(1,N):
        result = 0
        for j in range(0, i):
            # nums[i]보다 이전의 값들과 비교해서 상대적으로 nums[i]가 클 때만 +1을 result와 비교함.
            if nums[j] < nums[i]:
                result = max(result, dp[j]+1)
            # 작을 경우엔 +1을 할 수 없으니 dp[j]를 비교하는 것임.
            else:
                result = max(result, dp[j])

        # 비교가 끝나면 dp[i]에 result값(가장 최대의 경우)을 넣어줌.
        dp[i] = result

    return dp[N-1]

print(solution([1,4,2,3,1,5,7,3]))
print(solution([1,2,3,34,5,5]))
print(solution([3,2,1]))
        