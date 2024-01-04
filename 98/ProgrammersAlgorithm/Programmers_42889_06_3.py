def solution(N, stages):
    total = len(stages)
    challenging = [0] * N
    for i in range(total):
        if stages[i] > N:
            continue
        else:
            challenging[stages[i]-1] += 1
    
    fail_percentage = [0.0] * (N + 1)

    for i in range(1, N+1):
        
        # 문제된 부분은 아무도 단계에 도달해보지 못한 경우 도전자가 0일 때였음.
        # (ZeroDivisionError: division by zero) 가 뜨게 되어 문제가 됨. 이런 경우를 방지해보고자 Test Case 추가를 해두게 됨.
        if total == 0:
            fail_percentage[i] = 0
            continue
        fail_percentage[i] = challenging[i-1] / total
        total -= challenging[i-1]
        
    result = sorted(range(1, N + 1), key = lambda x: fail_percentage[x], reverse = True)
    return result