import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

square = [[0] * M for i in range(N)]

for i in range(N):
    square[i] = list(map(int, input().rstrip()))

max_len = min(N,M)

for size in range(max_len, 0, -1):
    for j in range(0, M-size+1):
        for i in range(0, N-size+1):
            # Tip: python에서는 하단과 같이 여러 식의 동등여부를 chained comparison이라는 걸 제공하여 검사가능함.
            if square[i][j] == square[i][j+size-1] == square[i+size-1][j] == square[i+size-1][j+size-1]:
                print(size**2)
                exit()
