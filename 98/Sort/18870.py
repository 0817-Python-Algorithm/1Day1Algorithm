import sys

input = sys.stdin.readline

N = int(input())

X = [int(str) for str in input().rstrip().split(" ")]
set_X = set(X)
filtered_X = sorted(list(set_X))
count = {}
for i in range(len(filtered_X)):
    if count.get(filtered_X[i], -1) == -1:
        count[filtered_X[i]] = i

for x in X:
    print(count.get(x), end = " ")