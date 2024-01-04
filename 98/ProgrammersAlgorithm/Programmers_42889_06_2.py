
# 런타임에러가 뜨길래 이중 for문을 단축해야 했음. M + NlogN을 맞추기 위해
# 이중 for문을 해제하고, 순차적으로 값을 삭제하는 코드를 짜게 됨.(total -= challenging[i-1])

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
        fail_percentage[i] = challenging[i-1] / total
        total -= challenging[i-1]

    result = sorted(range(1, N + 1), key = lambda x: fail_percentage[x], reverse = True)
    return result

print(solution(5, [2,1,2,6,2,4,3,3]))