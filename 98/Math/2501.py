import sys

result = 0
count = 0
N, K = map(int, sys.stdin.readline().split())
for i in range(1, N + 1, 1):

    if N % i == 0:
        result = i
        count += 1
    if count == K:
        print(i)
        exit()
print(0)
