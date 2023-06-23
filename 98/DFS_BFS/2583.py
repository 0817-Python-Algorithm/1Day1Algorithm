import sys

sys.setrecursionlimit(100000)
m, n, k = map(int, sys.stdin.readline().split())
square = [[False] * m for _ in range(n)]


# 사각형 파트를 색칠하는 함수
def tint(coordinate):
    for i in range(coordinate[0], coordinate[2]):
        for j in range(coordinate[1], coordinate[3]):
            print(i, j)
            square[i][j] = True


# 사각형 파트는 모두 색칠해버림
for _ in range(k):
    coordinate_temp = list(map(int, sys.stdin.readline().split()))
    tint(coordinate_temp)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(a, b):
    global count
    global square
    square[a][b] = True
    for idx in range(4):
        nx = a + dx[idx]
        ny = b + dy[idx]
        if 0 <= nx < n and 0 <= ny < m and not square[nx][ny]:
            count += 1
            dfs(nx, ny)


part = 0
count = 1
ans = []

for i in range(n):
    for j in range(m):
        if not square[i][j]:
            part += 1
            dfs(i, j)
            ans.append(count)
            count = 1
ans.sort()
print(part)
print(" ".join(map(str, ans)))
