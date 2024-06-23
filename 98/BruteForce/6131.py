import sys
input = sys.stdin.readline

N = int(input())

total = 0

for i in range(1, 501):
    for j in range(1, i):
        if i**2 - j**2 == N:
            total += 1
print(total)