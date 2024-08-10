import sys
input = sys.stdin.readline

V, E = map(int, input().split(" "))

edges = []
root = [i for i in range(0, V+1)]
result = 0


for _ in range(E):
    A,B,C = map(int, input().split(" "))
    edges.append((C,A,B)) # 가중치(C)를 기준으로 정렬하기 위해서 순서 변경
edges.sort()

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x1 = find(x)
    y1 = find(y)
    
    if x1 < y1:
        root[y1] = x1
    else:
        root[x1] = y1

def isConnected(x,y):
    x1 = find(x)
    y1 = find(y)
    
    if x1 == y1:
        return True
    else:
        return False
    
count = 0

for edge in edges:
    if count == V - 1:
        break
    if not isConnected(edge[1], edge[2]):
        union(edge[1], edge[2])
        result += edge[0]
        count += 1

print(result)