import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

numbers = [0] + list(map(int, input().rstrip().split(" ")))

for i in range(1, N+1):
    numbers[i] += numbers[i-1]

for i in range(M):
    i,j = map(int, input().rstrip().split(" "))
    print(numbers[j]-numbers[i-1])