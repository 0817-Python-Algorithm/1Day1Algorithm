import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

n, m = map(int, input().rstrip().split())

parent = [i for i in range(0, n+1)]

def find_root(index):
    if parent[index] == index:
        return index
    else:
        parent[index] = find_root(parent[index])
        return parent[index]
    
def combine(a, b):
    parent[find_root(b)] = find_root(a)

for _ in range(m):
    cal, a, b = map(int, input().rstrip().split())
    if cal == 0:
        combine(a, b)
    else:
        if find_root(a) == find_root(b):
            print("YES")
        else:
            print("NO")