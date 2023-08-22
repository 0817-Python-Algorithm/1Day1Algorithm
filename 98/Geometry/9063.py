import sys

num = int(sys.stdin.readline().strip())
if num == 1:
    print(0)
    exit(0)
max_x = -10000
max_y = -10000
min_x = 10000
min_y = 10000
for _ in range(num):
    x,y = map(int, sys.stdin.readline().strip().split())
    max_x = max(max_x,x)
    min_x = min(min_x,x)
    max_y = max(max_y,y)
    min_y = min(min_y,y)
print((max_x-min_x)*(max_y-min_y))
    