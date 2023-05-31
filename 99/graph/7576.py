from collections import deque
def bfs():
    max = 1
    while(len(q) != 0):
        pos = q.popleft()
        for d in dir:
            next_pos = [x+y for x,y in zip(pos, d)]
            if 0 <= next_pos[0] <height and 0 <= next_pos[1] < width and tomatos[next_pos[0]][next_pos[1]] == 0:
                q.append(next_pos)
                tomatos[next_pos[0]][next_pos[1]] = tomatos[pos[0]][pos[1]] + 1
                if max < tomatos[pos[0]][pos[1]] + 1:
                    max = tomatos[pos[0]][pos[1]] + 1
    return max
width, height = map(int, input().split())
tomatos = [list(map(int, input().split())) for i in range(height)]
q = deque([])
dir = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(height):
    for j in range(width):
        if tomatos[i][j] == 1:
            q.append((i,j))

max = bfs()
for row in tomatos:
    for x in row:
        if x == 0:
            max = 0

print(max-1)