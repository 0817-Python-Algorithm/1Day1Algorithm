import sys
from collections import deque

n = int(sys.stdin.readline())
S = []
for _ in range(n):
    S.append(deque(sys.stdin.readline().strip().split()))

S_length = 0
for i in range(n):
    S_length += len(S[i])

L = sys.stdin.readline().strip().split()
if len(list(L))!=S_length:
    print("Impossible")
    exit()
for i in list(L):
    for j in range(n):
        if len(S[j]) == 0:
            continue
        if S[j][0] == i:
            S[j].popleft()
            break
        if j == n-1:
            print("Impossible")
            exit()
print("Possible")