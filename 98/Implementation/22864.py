import sys
input = sys.stdin.readline().rstrip

A, B, C, M = map(int, input().split(" "))
hp = 0
completed = 0
for i in range(24):
    if hp + A <= M:
       completed += B
       hp += A
    else:
        if hp < C:
            hp = 0
        else: 
            hp -= C

print(completed)