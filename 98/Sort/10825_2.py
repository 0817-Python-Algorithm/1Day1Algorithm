import sys
input = sys.stdin.readline

N = int(input())
info = []
for i in range(N):
    arr = input().rstrip().split(" ")
    # 튜플을 활용해서 서로 다른 타입들을 하나로 묶을 수 있음.
    # *을 map 앞에 써서 map을 풀어서 넣어주기가 가능
    info.append((arr[0], *map(int, arr[1:4])))

# lambda를 활용해서 -는 내림차순, +는 오름차순으로 구현하기
info.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in info:
    print(i[0])