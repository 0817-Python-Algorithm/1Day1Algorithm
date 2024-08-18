import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0

for i in range(1, N):
    for j in range(0, N-i):
        if A[j] > A[j+1]:
            count += 1
            A[j], A[j+1] = A[j+1], A[j]
            if count == K:
                print(A[j], A[j+1])
                sys.exit()
print(-1)