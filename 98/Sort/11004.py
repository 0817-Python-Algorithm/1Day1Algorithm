import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(N-1, 0, -1):
    for j in range(0, i, 1):
        if A[j]> A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
print(A[K-1])