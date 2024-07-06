import sys

input = sys.stdin.readline

n,m = map(int, input().rstrip().split(" "))

T = list(map(int, input().rstrip().split(" ")))

start = 0
end = start + m - 1
benefit = sum(T[start:end+1])

max_benefit = 0

while True:
    max_benefit = max(max_benefit, benefit)
    benefit -= T[start]
    start += 1
    end += 1
    if end == n:
        break
    benefit += T[end]
    
print(max_benefit)
    
    