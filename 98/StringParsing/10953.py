import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    A,B = map(int, input().rstrip().split(","))
    print(A+B)