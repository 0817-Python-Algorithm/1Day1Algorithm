import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()

def isEmpty(queue):
    return True if len(queue) == 0 else False

# functions = {'push_back': function_1,
#              'push_front': function_2,
#              'c': self.method_1, ...}
# 위와 같은 방식으로 function Dictionary 생성하기

for i in range(N):
    c = input().rstrip().split(" ")
    if c[0] == "push_back":
        queue.append(c[1])
    elif c[0] == "push_front":
        queue.appendleft(c[1])
    elif c[0] == "pop_front":
        print(-1) if isEmpty(queue) else print(queue.popleft())
    elif c[0] == "pop_back":
        print(-1) if isEmpty(queue) else print(queue.pop())
    elif c[0] == "size":
        print(len(queue))
    elif c[0] == "empty":
        print(1) if isEmpty(queue) else print(0)
    elif c[0] == "front":
        print(-1) if isEmpty(queue) else print(queue[0])
    elif c[0] == "back":
        print(-1) if isEmpty(queue) else print(queue[-1])
    
    


