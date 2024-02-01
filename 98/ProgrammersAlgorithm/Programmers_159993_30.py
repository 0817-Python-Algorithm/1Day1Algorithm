from collections import deque

def solution(maps):
    INF = 1_000_000
    N = len(maps)
    M = len(maps[0])
    non_visit = deque()
    way = [[INF]* (M+1) for _ in range(N+1)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    start = [0,0]
    lever = [0,0]
    end = [0,0]
    
    for i in range(0,N):
        for j in range(0,M):
            if maps[i][j] == "S":
                start = [i+1,j+1]
            elif maps[i][j] == "L":
                lever = [i+1,j+1]
            elif maps[i][j] == "E":
                end = [i+1,j+1]
            non_visit.append([i+1,j+1])

    way[start[0]][start[1]] = 0
    non_visit.remove(start)
    non_visit.appendleft(start)

    while non_visit:
        location = non_visit.popleft()
        for i in range(4):
            x = location[0] + dx[i]
            y = location[1] + dy[i]
            
            if x == 0 or y == 0 or x > N or y > M:
                continue
            if maps[x-1][y-1] == "X":
                continue
            way[x][y] = min(way[x][y], way[location[0]][location[1]]+1)
        non_visit = deque(sorted(non_visit, key=lambda x: way[x[0]][x[1]]))
    
    non_visit = deque()
    way2 = [[INF] * (M+1) for _ in range(N+1)]
    
    for i in range(0,N):
        for j in range(0,M):
            non_visit.append([i+1,j+1])

    way2[lever[0]][lever[1]] = 0
    non_visit.remove(lever)
    non_visit.appendleft(lever)

    while non_visit:
        location = non_visit.popleft()
        for i in range(4):
            x = location[0] + dx[i]
            y = location[1] + dy[i]
            if x == 0 or y == 0 or x > N or y > M or location == [x,y]:
                continue
            if maps[x-1][y-1] == "X":
                continue
            way2[x][y] = min(way2[x][y], way2[location[0]][location[1]]+1)
        non_visit = deque(sorted(non_visit, key=lambda x: way2[x[0]][x[1]]))

    if not way[lever[0]][lever[1]] < INF or not way2[end[0]][end[1]] < INF:
        return -1
    else:
        return way[lever[0]][lever[1]] + way2[end[0]][end[1]]

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
print(solution(["SOEOL","XXXXO","OOOOO","OXXXX","OOOOO"]))
print(solution(["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"]))
print(solution(["OOOOOL", "OXOXOO", "OOSXOX", "OXXXOX", "EOOOOX"]))
print(solution(["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"]))
print(solution(["SELXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]))