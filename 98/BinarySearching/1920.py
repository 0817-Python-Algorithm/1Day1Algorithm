import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split(" ")))

M = int(input())
nums = list(map(int, input().split(" ")))

for num in nums:
    if bisect_right(A, num) > 0 and bisect_left(A, num) < N:
        if num == A[bisect_left(A, num)]:
            print(1)
        else:
            print(0)
    else:
        print(0)