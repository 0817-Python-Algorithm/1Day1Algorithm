import sys
result = 0
n = sys.stdin.readline().rstrip()
arr = list(map(int, sys.stdin.readline().rstrip().split()))

temp1 = sum(arr)**2
temp2 = sum(i**2 for i in arr)
print((temp1-temp2)//2)
