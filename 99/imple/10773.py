from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
q = deque()
for i in range(N):
    num = int(input())
    if num != 0:
        q.append(num)
    else:
        q.pop()
print(sum(q))