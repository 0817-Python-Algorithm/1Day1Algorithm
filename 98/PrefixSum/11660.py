import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

nums = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    temp = [0] + list(map(int, input().rstrip().split(" ")))
    for j in range(1, N+1):
        nums[i][j] = nums[i-1][j] + nums[i][j-1] - nums[i-1][j-1] + temp[j]


for i in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split(" "))
    print(nums[x2][y2] - nums[x1-1][y2] - nums[x2][y1-1] + nums[x1-1][y1-1])