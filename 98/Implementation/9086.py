import sys

n = int(sys.stdin.readline().rstrip())
array = []
for _ in range(n):
    temp = list(sys.stdin.readline().rstrip())
    print(temp[0] + temp[-1])
