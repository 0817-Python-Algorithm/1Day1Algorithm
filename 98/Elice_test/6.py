import sys
input = sys.stdin.readline

def length(str):
    return [len(i) for i in str]

N = int(input())
color = list(map(int, input().split(" ")))

node = [[i] for i in range(N)]

for i in range(N):
    node.sort(key=len)
    if color[i] == 1:
        node.remove(node[-1])
        
        