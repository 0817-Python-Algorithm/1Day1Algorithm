def solution(money):
    N = len(money)
    dp1_yes = [0] * N
    dp1_no = [0] * N
    
    dp1_yes[0] = money[0]
    dp1_yes[1] = money[0]
    dp1_no[0] = 0
    dp1_no[1] = money[1]
    for i in range(2, N-1):
        dp1_yes[i] = dp1_no[i-1] + money[i]
        dp1_no[i] = max(dp1_no[i-1], dp1_no[i-2]+money[i])
    dp1_yes[N-1] = dp1_no[N-]
    
    for i in range():
        
    

    answer = 0
    return answer


