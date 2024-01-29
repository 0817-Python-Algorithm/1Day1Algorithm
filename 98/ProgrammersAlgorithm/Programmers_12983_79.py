def solution(strs, t):
    N = len(t)
    dp = [len(t)] * N
    
    dictionary = {}
    for str in strs:
        dictionary[str] = 1
    
    if t[0] in dictionary:
        dp[0] = 1
    for i in range(1,N):
        if t[0:i+1] in dictionary:
            dp[i] = dictionary[t[0:i+1]]
            continue
        if i < 5:
            for j in range(0,i):
                if t[0:i-j] in dictionary and t[i-j:i+1] in dictionary:
                    dp[i] = min(dp[i], dictionary[t[0:i-j]]+dictionary[t[i-j:i+1]])
        else:
            for j in range(5):
                if t[0:i-j] in dictionary and t[i-j:i+1] in dictionary:
                    dp[i] = min(dp[i], dictionary[t[0:i-j]]+dictionary[t[i-j:i+1]])
                elif t[0:j+1] in dictionary and t[j+1:i+1] in dictionary:
                    dp[i] = min(dp[i], dictionary[t[0:j+1]]+dictionary[t[j+1:i+1]])
        if t[:i+1] not in dictionary:
            dictionary[t[:i+1]] = dp[i]
    
    if dp[N-1] == N:
        return -1
    else:
        answer = dp[N-1]

    return answer

# 이 풀이는 틀린 풀이임, 계산 시 효율성 테스트를 통과할 수가 없는 형태임.
# 시간 복잡도는 O(N^2)임.

print(solution(["ba","na","n","a"],"banana"))
print(solution(["app","ap","p","l","e","ple","pp"],"apple"))
print(solution(["ba","an","nan","ban","n"],"banana"))

