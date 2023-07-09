import sys
input = sys.stdin.readline
r,c = map(int,input().split())
paper = []
for _ in range(r):
    paper.append(list(map(int,input().split())))
max_val= 0
isVisited = [[False] * c for _ in range(r)]
def dfs(row,col,sum,depth):
    global max_val
    if depth == 4:
        max_val = max(max_val, sum)
        return
    isVisited[row][col] = True
    if col + 1 < c and isVisited[row][col+1] == False:
        dfs(row,col+1, sum+paper[row][col+1],depth+1)
    if row+1 < r and isVisited[row+1][col] == False:
        dfs(row+1, col, sum+paper[row+1][col],depth+1)
    if col-1 >= 0 and isVisited[row][col-1] == False:
        dfs(row, col-1, sum+paper[row][col-1],depth+1)
    if row-1 >= 0 and isVisited[row-1][col] == False:
        dfs(row-1, col, sum+paper[row-1][col],depth+1)
    isVisited[row][col] = False
d = ((1,0),(0,1),(-1,0),(0,-1))
for i in range(r):
    for j in range(c):
        dfs(i,j,paper[i][j],1)
        for k in range(4):
            points = []
            points.append((d[k%4][0] + i, d[k%4][1] + j))
            points.append((d[(k+1)%4][0] + i, d[(k+1)%4][1] + j))
            points.append((d[(k+2)%4][0] + i, d[(k+2)%4][1] + j))
            tmp = paper[i][j]
            for point in points:
                if 0<=point[0]<r and 0<=point[1]<c:
                    tmp += paper[point[0]][point[1]]
            max_val = max(max_val,tmp)
print(max_val)