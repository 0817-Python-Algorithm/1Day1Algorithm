# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    length = len(priorities)
    queue = deque(priorities)
    index_queue = deque(range(length))
    order = []
    while queue:
        m = max(queue)
        if queue[0] == m:
            order.append(index_queue[0])
            queue.popleft()
            index_queue.popleft()
        else:
            queue.append(queue.popleft())
            index_queue.append(index_queue.popleft())
    for i in range(length):
        if order[i] == location:
            answer = i + 1
    
    
    return answer

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))