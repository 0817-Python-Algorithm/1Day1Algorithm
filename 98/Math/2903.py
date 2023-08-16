import sys

N = int(sys.stdin.readline())
point = 2
for _ in range(N):
    point += (point-1)
print(point**2)