import sys
input = sys.stdin.readline

K = int(input())
number = int(input(), 2)

for i in range(1, K+1):
    for j in range(0, i+1):
        plus = i - j
        multiple = j
        
        if (number + plus) * (2**multiple) % (2**K) == 0:
            print(i)
            sys.exit()
    