import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(",")))
B = []
for i in range(K):
    for i in range(N-i-1):
        B.append(A[i+1]-A[i])
    A = B
    B = []
print(",".join(map(str,A)))