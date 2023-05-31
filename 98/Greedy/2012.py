import sys

ip = sys.stdin.readline
n = int(ip())
scores = []
for _ in range(n):
    scores.append(int(ip()))
scores.sort()
count = 0
for idx in range(1, n + 1):
    count += abs(scores[idx - 1] - idx)
print(count)
