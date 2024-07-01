import sys
input = sys.stdin.readline

N = int(input())

meetings = []
for i in range(N):
    meetings.append(list(map(int, input().rstrip().split(" "))))

meetings.sort(key = lambda x: (x[1],x[0]))

enable_time = 0
count = 0

for meeting in meetings:
    if meeting[0] >= enable_time:
        count += 1
        enable_time = meeting[1]
        
print(count)