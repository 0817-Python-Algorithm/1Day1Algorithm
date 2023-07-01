from collections import deque
T = int(input())
for _ in range(T):
    N, index = map(int,input().split())
    q = deque(list(map(int,input().split())))
    count = 1
    while(q):
        top = q[0]
        if max(q) == top:
            if index == 0:
                print(count)
                break
            else:
                count +=1
                index -= 1
        else:
            if index == 0:
                index = len(q)-1
            else:
                index -= 1
            q.append(top)
        q.popleft()