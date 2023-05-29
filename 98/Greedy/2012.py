n = int(input())
scores=[]
for i in range(n):
    scores.append(int(input()))
scores.sort()
count = 0
for idx in range(1, n+1):
    count += abs(scores[idx-1]-idx)
print(count)