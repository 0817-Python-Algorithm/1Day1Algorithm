import sys

input = sys.stdin.readline().rstrip

A, B, V = list(map(int, input().split(" ")))

day = 0

# 미리 A만큼 빼두고서 계산을 해야 처음에 한번에 올라가는 걸 방지할 수 있음.
day += (V-A) // (A-B) + 1

# 만약 나머지가 남는다는 것은 마지막에 올라갈 때 도착지점을 넘어서 올라가는 경우임.
if (V-A) % (A-B) != 0:
    day += 1

print(day)