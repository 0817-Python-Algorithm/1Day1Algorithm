from collections import deque

def solution(progresses, speeds):
    
    # 작업들을 deque에 순서대로 추가하는 작업
    queue = deque(progresses)
    speedQueue = deque(speeds)
    answer = []
    
    
    while len(queue) > 0:
        count = 0
        for i in range(len(speedQueue)):
            queue[i] += speedQueue[i]
        while queue and queue[0] >= 100:
            queue.popleft()
            speedQueue.popleft()
            count += 1
        if count > 0:
            answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 솔직히 이 문제를 deque를 활용해서 풀어야 하는 이유는 모르겠다.
# 전체적으로 queue없이도 값을 -1로 표시하여 비었다는 것을 표기한다면 차라리 deque를 import할 필요없이 구현이 가능할 것 같다.
