from collections import deque
N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
res = []
q = deque(arr)
while(q):
    for _ in range(K-1):
        q.append(q.popleft())
    res.append(q.popleft())
print('<',end='')
for i in res[:-1]:
    print(str(i)+', ',end='')
print(str(res[-1])+'>')