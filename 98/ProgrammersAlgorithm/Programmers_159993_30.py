from collections import deque

def solution(maps):
    INF = 1_000_000
    N = len(maps)
    M = len(maps[0])
    list = deque()
    visit = [[False]*(M+1) for _ in range(N+1)]
    way = [[INF]* (M+1) for _ in range(N+1)]
    way2 = [[INF] * (M+1) for _ in range(N+1)]

    result1 = INF
    result2 = INF

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

    # start -> lever 가는 경우를 계산
    way[start[0]][start[1]] = 0
    non_visit = deque([start])

    while non_visit:
        location = non_visit.popleft()
        # location을 기준으로 상하좌우를 돎.
        for i in range(4):
            x = location[0] + dx[i]
            y = location[1] + dy[i]

            # 만약 해당 위치가 사각형을 벗어난다면 continue
            if not (0 < x <= N and 0 < y <= M):
                continue

            # 만약 해당 위치가 문제에서 주어지는 갈 수 없는 영역("X")라면 continue
            if maps[x-1][y-1] == "X":
                continue

            # 만약 해당 위치가 location에서 이동해서 가는 경우보다 값이 크면 업데이트하고 non_visit에 추가
            if way[x][y] > way[location[0]][location[1]] + 1:
                way[x][y] = way[location[0]][location[1]] + 1
                if [x,y] == lever:
                    result1 = way[x][y]
                    
                non_visit.append([x,y])



    # 여기부터는 lever -> end로 가는 경우를 계산
    # 계산 방식은 앞서 한 것과 동일함.

    way2[lever[0]][lever[1]] = 0
    
    non_visit.append(lever)

    while non_visit:
        location = non_visit.popleft()
        for i in range(4):
            x = location[0] + dx[i]
            y = location[1] + dy[i]
            if x == 0 or y == 0 or x > N or y > M or location == [x,y]:
                continue
            if maps[x-1][y-1] == "X":
                continue
            if way2[x][y] > way2[location[0]][location[1]] + 1:
                way2[x][y] = way2[location[0]][location[1]] + 1
                if [x,y] == end:
                    result2 = way2[x][y]

                non_visit.append([x,y])


    if not way[lever[0]][lever[1]] < INF or not way2[end[0]][end[1]] < INF:
        return -1
    else:
        return result1 + result2
    

# 솔직히 이 문제 무척 고민도 많이 하고 오래 걸려 푼 문제임.
# 다익스트라 알고리즘을 쓸 생각을 못했었고 그 결과 어떤 방식으로 풀이할 지를 가닥을 잡아도 시간복잡도가 말도 안되게 올라가는 이슈가 발생함.
# 문제 풀이 방식에는 무리가 없었지만 계속해서 정렬을 하는 방식이 꽤나 무거운 과정으로 동작하게 됨.
# 정렬하는 과정을 줄이고 단순히 돌아야 할 방향들을 계속 non_visit에 넣는 과정이 이것을 해소해주었음.

# 1.다익스트라 알고리즘을 적용하고,
# 2.필요한 연산만을 계산에 포함하는 것이 중요함을 알게됨.

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
print(solution(["SOEOL","XXXXO","OOOOO","OXXXX","OOOOO"]))
print(solution(["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"]))
print(solution(["OOOOOL", "OXOXOO", "OOSXOX", "OXXXOX", "EOOOOX"]))
print(solution(["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"]))
print(solution(["SELXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]))