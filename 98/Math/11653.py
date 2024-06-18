import sys
input = sys.stdin.readline

N = int(input())
total = N
for i in range(2, N+1):
    while True:
        if total == 1:
            break
        if total % i == 0:
            total /= i
            print(i)
        else:
            break
    if total == 1:
        break
        