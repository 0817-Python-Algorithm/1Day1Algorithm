def solution(money):
    N = len(money)
    
    # dp1_yes[i]는 index=0인 집을 털었을 때 index=i인 집까지 계산 시 최대 털은 금액을 의미.
    # dp1_no[i]는 index=0인 집을 털지 않았을 때 index=i인 집까지 계산 시 최대 털은 금액을 의미.
    dp1_yes = [0] * N
    dp1_no = [0] * N
    
    # 0번째 집을 털었을 때 0번째까지 턴 최대 금액은 money[0]이 다임.
    dp1_yes[0] = money[0]
    # 0번째 집을 털었을 때 1번째까지 턴 최대 금액은 money[0]이 다임. 왜냐하면 1번째 집은 털 수가 없기 때문(dp1_yes 자체가 0번째집을 턴다는 전제니까.)
    dp1_yes[1] = money[0]
    # 0번째 집을 안 털었을 때 0번째까지 턴 최대 금액은 0원임.(못터니까)
    dp1_no[0] = 0
    # 0번째 집을 안 털었을 때 1번째까지 턴 최대 금액은 money[1]임.(0번째 집을 안 털었으니 1번째 집이라도 털어야 최대 금액이 되니까.)
    dp1_no[1] = money[1]
    
    for i in range(2, N-1):
        dp1_yes[i] = max(dp1_yes[i-2] + money[i], dp1_yes[i-1])
        dp1_no[i] = max(dp1_no[i-2]+money[i], dp1_no[i-1])
        
    dp1_yes[N-1] = dp1_yes[N-2]
    dp1_no[N-1] = max(dp1_no[N-3] + money[N-1], dp1_no[N-2])
    
    answer = max(dp1_yes[N-1], dp1_no[N-1])
    
    return answer

# 이 문제의 핵심은 집이 원형으로 짜여져있기에 첫 시작점을 털었냐 말았냐에 따라 마지막점을 털 수 있냐 마냐가 결정된다는 점임.
# 그래서 dp를 dp1_yes, dp1_no로 나눠서 경우에 따라 계산을 해준 뒤 두 값을 N-1까지 했을 때 결과 중 max 값을 answer로 잡아야 함.
# 이 생각이 생각보다는 쉽지만 나눌 생각까지를 못했음.

print(solution([1, 2, 3, 1]))
print(solution([1,10,1,1,1,1,1,1,0,1,1,1]))
