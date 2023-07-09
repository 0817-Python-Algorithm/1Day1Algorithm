import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
set_S = []
for _ in range(N):
    arr.append(sys.stdin.readline().strip())
for _ in range(M):
    set_S.append(sys.stdin.readline().strip())
count = 0
for s in set_S:
    if s in arr:
        count += 1
print(count)
