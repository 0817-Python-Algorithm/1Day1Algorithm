def solution(progresses, speeds):
    
    # 리스트에는 맨 뒤를 pop하는 내장 함수밖에 업기 때문에 reversed로 배열을 뒤집어주는 작업을 진행함.
    p = list(reversed(progresses))
    s = list(reversed(speeds))
    answer = []

    while p:
        count = 0
        for i in range(len(p)):
            p[i] += s[i]
        while p and p[-1] >= 100:
            p.pop()
            s.pop()
            count += 1

        # count가 0이라면 아무것도 배포할 수 없기 때문에 0보다 클 경우(배포한게 1개라도 있을 때) append함.
        if count > 0:
            answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))