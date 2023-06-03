n = int(input())
x,y = 1,1
arrows = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
arrow_str = ["L","R","U","D"]
for arrow in arrows:
  for i in range(len(arrow_str)):
    if arrow == arrow_str[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx <1 or nx>n or ny<1 or ny>n:
    continue
  x = nx
  y = ny
print(x, y)