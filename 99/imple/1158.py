from collections import deque
N,K = map(int,input().split())
q = [i+1 for i in range(N)]
q = deque(q)
answer = []
while(q):
    for _ in range(K):
        person = q.popleft()
        q.append(person)
    answer.append(q.pop())
print('<'+str(answer[0]),end='')
for i in answer[1:]:
    print(', '+str(i),end='')
print('>')

    