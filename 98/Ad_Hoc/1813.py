import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split(" ")))

arr = [0]*51

for num in nums:
    arr[num] += 1
for i in range(50, -1, -1):
    if arr[i] == i:
        print(i)
        sys.exit()
print(-1)

