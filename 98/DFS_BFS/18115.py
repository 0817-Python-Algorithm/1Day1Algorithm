from collections import deque
import sys

order = deque()
n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
cards = cards[::-1]

num = 1
for card in cards:
    if card == 1:
        order.appendleft(num)
        num += 1
    if card == 2:
        temp = order.popleft()
        order.appendleft(num)
        order.appendleft(temp)
        num += 1
    if card == 3:
        order.append(num)
        num += 1
for i in order:
    print(i, end=" ")
