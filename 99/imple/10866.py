from collections import deque
import sys
input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    line = input().split()
    if line[0] == 'push_back':
        q.append(line[1])
    elif line[0] == 'push_front':
        q.appendleft(line[1])
    elif line[0] == 'front':
        print(q[0] if q else -1)
    elif line[0] == 'back':
        print(q[-1] if q else -1)
    elif line[0] == 'pop_front':
        print(q.popleft() if q else -1)
    elif line[0] == 'pop_back':
        print(q.pop() if q else -1)
    elif line[0] == 'empty':
        print(0 if q else 1)
    else:
        print(len(q))