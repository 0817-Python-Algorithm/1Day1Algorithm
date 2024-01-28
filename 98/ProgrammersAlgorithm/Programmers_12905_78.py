def solution(board):
    
    row = len(board)
    col = len(board[0])
    
    dp = [[0]* col for _ in range(row)]
    
    dp = list(board)

    for i in range(1,row):
        for j in range(1,col):
            if dp[i][j] == 1:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                
    # 이 부분에서 문제가 생겼었음.
    # 다음 줄을 M = max(max(i for i in dp))로 푸니 효율성이나 정답에 있어서 틀리는 이슈가 발생했음.
    # 왜 그런지는 추후 알아봐야겠음.
    M = max(max(i) for i in dp)
    answer = M**2

    return answer

# 일단 처음엔 정사각형을 만든다는 생각을 못했음.
# 직사각형을 만들 생각만 하고 있었는데 구현을 하다보니 이 부분은 더 어렵겠다는 생각음 함.
# 처음 풀이는 해당 지점이 색이 칠해져 있을 때 행만, 열만 봤을 때 최대 연결되는 길이를 배열로 넣어두었음.
# 하지만, 이 경우 1가로,1세로만 채워지고 나머지는 안 채워지는 이슈가 발생함.
# 여기서 다시 돌아와 풀어보니 정사각형을 구하는 것을 알게 됨.
# 이때 어떤 지점의 위, 왼쪽, 좌대각선 위가 어느 크기의 정사각형을 만들 수 있는지를 확인해보고 최솟값에 1을 더하면 정사각형을 만드는게 보장이 되는 것을 알게 됨.


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))