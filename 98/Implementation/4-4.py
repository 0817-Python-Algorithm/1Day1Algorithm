import sys

h, w = map(int, sys.stdin.readline().split())
place = []

x, y, d = map(int, sys.stdin.readline().split())
for i in range(h):
    place.append(list(map(int, sys.stdin.readline().split())))
visit = [[0] * w for _ in range(h)]
visit[x][y] = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def turn_left():
    global d
    d += 1
    d %= 4


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if place[nx][ny] == 0 and visit[nx][ny] == 0:
        visit[nx][ny] = 1
        count += 1
        turn_time = 0
        x = nx
        y = ny
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x + dx[d]
        ny = y + dy[d]
        if place[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break
print(count)