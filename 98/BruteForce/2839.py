import sys

input = sys.stdin.readline

N = int(input())

result = N // 3 + 1

for i in range(N // 3, -1, -1):
    if (N - 3 * i) % 5 == 0:
        result = i + (N - 3 * i) // 5

if result == N // 3 + 1:
    print(-1)
else:
    print(result)