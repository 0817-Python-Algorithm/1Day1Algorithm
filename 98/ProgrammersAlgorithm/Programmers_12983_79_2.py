def solution(strs, t):
    N = len(t)
    INF = 100000
    dp = [INF] * (N+1)
    sizes = set(len(str) for str in strs)
    
    for i in range(1,N+1):
        if t[:i] in strs:
                dp[i] = 1
                continue
        for size in sizes:
            if i > size and t[i-size:i] in strs:
                dp[i] = min(dp[i], dp[i-size]+1)
    return dp[N] if dp[N] != INF else -1
                     
# 이 문제에서 정말 오랜 시간이 걸렸음.
# 문제 중 풀리지 않는 부분이 17번 테스트 하나였는데 이 부분에 대한 디버깅을 하는데에 오래 걸렸음.
# 해당 테스트 케이스가 무엇인지는 정확히는 모르겠지만 추측하기로는 현재 이 코드의 맨 마지막과 같은 상황일 것 같음.
# dp에 초기화 시켜두는 값이 INF가 아니고 N으로 했던 점이 문제였던 것으로 보임.
# 만약 t의 길이가 1이면 1로 도배되는데 이것이 우연히 최소 조합 개수와도 일치할 수 있기 때문이었음.

# 앞으로는 본인 판단 하에 최댓값이라고 생각하는 정도가 아닌 문제에 영향을 끼치지 않는 선에서의 INF값을 설정해야겠다고 판단함.
print(solution(["ba","na","n","a"],"banana"))
print(solution(["app","ap","p","l","e","ple","pp"],"apple"))
print(solution(["ba","an","nan","ban","n"],"banana"))
print(solution(["ba","b"],"b"))

