import sys
input = sys.stdin.readline

white = 0
blue = 0

def partition(x,y,d):
    color = paper[x][y]
    for i in range(x, x+d):
        for j in range(y, y+d):
            if color != paper[i][j]:
                partition(x,y,d//2)
                partition(x+d//2,y,d//2)
                partition(x,y+d//2,d//2)
                partition(x+d//2,y+d//2,d//2)
                return
    if color == 0:
        global white
        white += 1
    else:
        global blue
        blue += 1
                

N = int(input())

paper = [[0] * N for _ in range(N)]

for i in range(N):
    paper[i] = list(map(int, input().rstrip().split(" ")))

partition(0,0,N)

print(white)
print(blue)