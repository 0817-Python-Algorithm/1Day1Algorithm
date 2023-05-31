import copy
from collections import deque
height, width = map(int, input().split())
map = [list(map(int, input().split())) for i in range(height)]
dir = [[-1,0],[1,0],[0,1],[0,-1]]
def bfs():
    cp_map = copy.deepcopy(map)
    q = deque()
    for i in range(height):
        for j in range(width):
            if cp_map[i][j] == 2:
                q.append((i,j))
    while(len(q) != 0):
        (curr_h, curr_w) = q.popleft()
        for d in dir:
            next_h = curr_h + d[0]
            next_w = curr_w + d[1]
            if 0<= next_h < height and 0<=next_w < width:
                if cp_map[next_h][next_w] == 0:
                    cp_map[next_h][next_w] = 2
                    q.append((next_h,next_w))
    count = 0
    global res
    for i in range(height):
        for j in range(width):
            if cp_map[i][j] == 0:
                count += 1
    res = max(count, res)

def wall(count):
    if count == 3:
        res = bfs()
        return
    for i in range(height):
        for j in range(width):
            if map[i][j] == 0:
                map[i][j] = 1
                wall(count+1)
                map[i][j] = 0
res = 0
wall(0)
print(res)