import sys
input = sys.stdin.readline

n,m = map(int, input().rstrip().split(" "))

arr = list(map(int, input().rstrip().split(" ")))

for _ in range(m):
    i,j,k = map(int, input().rstrip().split(" "))
    subArr = arr[i-1:j]
    subArr.sort()
    print(subArr[k-1])
    
