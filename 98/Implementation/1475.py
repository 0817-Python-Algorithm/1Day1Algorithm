import sys
import math
n = list(map(int, sys.stdin.readline().rstrip()))
result=[0]*10
for i in n:
    if i == 6 or i == 9:
        result[6] += 1
    else:
        result[i] += 1
result[6] = math.ceil(result[6]/2)
print(max(result))
