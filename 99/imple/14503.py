direction = ((-1,0),(0,1),(1,0),(0,-1))

N,M = map(int, input().split())
row,col, d = map(int,input().split())
room = []
count = 1
for _ in range(N):
    room.append(list(map(int,input().split())))
room[row][col] = 2
while(True):
    if room[row-1][col] !=0 and room[row][col+1]!=0 and room[row+1][col]!=0 and room[row][col-1]!=0:
        row = row - direction[d][0]
        col = col - direction[d][1]
        if room[row][col] == 1:
            print(count)
            break
    else:
        d = (d+3)%4
        next_row = row + direction[d][0]
        next_col = col + direction[d][1]
        if room[next_row][next_col] == 0:
            row = next_row
            col = next_col
            room[row][col] = 2
            count += 1