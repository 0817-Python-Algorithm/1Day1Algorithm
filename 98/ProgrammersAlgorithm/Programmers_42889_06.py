def solution(N, stages):
    stage_info = [[0, 0] for _ in range(N)]
    for i in range(len(stages)):
        if stages[i] > N:
            for j in range(N):
                stage_info[j][1] += 1
        else: 
            stage_info[stages[i]-1][0] += 1
            for j in range(stages[i]):
                stage_info[j][1] += 1

    fail_percentage = [0] * N
    for i in range(N):
        fail_percentage[i] = stage_info[i][0] / stage_info[i][1]
    

    # sorted 함수를 활용하면 정렬을 원하는 조건들을 끼워가면서 원하는 목록으로 할 수 있음.
    # 처음에는 정렬할 대상을, 중간에는 정렬할 방식(lambda 식으로), 마지막에는 오름-내림차순을 정할 수 있음.
    # 동일한 값에 대해선 먼저 온 값을 먼저 둠.
        
    # result = sorted(fail_percentage, reverse = True)
    result = sorted(range(1, N + 1), key=lambda x: fail_percentage[x-1], reverse=True)
    return result

print(solution(5, [2,1,2,6,2,4,3,3]))