# deque를 사용하려면 collections에서 import해다가 써야 함.
from collections import deque

def solution(N, K):
    arr = range(1, N+1)
    queue = deque(arr)
    
    # queue에 원소가 하나만 남을 때까지 돌림.
    while len(queue) > 1:
        # K-1회 원소를 빼서 뒤에 넣는 과정을 수행하고,
        for _ in range(K-1):
            queue.append(queue.popleft())
        # K번째의 원소를 pop함.
        queue.popleft()
    return queue[0]

print(solution(5,2))
print(solution(1,1))
print(solution(10,2))