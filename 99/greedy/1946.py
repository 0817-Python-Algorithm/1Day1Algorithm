import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank = sorted(rank, key=lambda x : x[0])
    count = 1
    top = rank[0]
    for x in rank[1:]:
        if top[1] > x[1]:
            count += 1
            top = x
    print(count)