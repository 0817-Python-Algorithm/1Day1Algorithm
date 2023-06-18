import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
fromIdx = 0
toIdx = 0
for i in range(N-1, 0, -1):
    maxIdx = arr.index(max(arr[0:i]))
    if arr[i]< arr[maxIdx]:
        count+=1
        arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
    if count == K:
        print(arr[maxIdx], arr[i])
        exit()
print(-1)
