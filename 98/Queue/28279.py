from collections import deque
import sys

testQueue = deque()
length = input()
for _ in range(int(length)):

    command = ''
    value = ''
    commandLine = list(map(int, sys.stdin.readline().strip().split()))
    command = commandLine[0]
    value = 0
    if len(commandLine) > 1:
        value = commandLine[1]

    if command == 1:
        testQueue.appendleft(value)
    elif command == 2:
        testQueue.append(value)
    elif command == 3:
        if len(testQueue) != 0:
            print(testQueue.popleft())
        else:
            print('-1')
    elif command == 4:
        if len(testQueue) != 0:
            print(testQueue.pop())
        else:
            print('-1')
    elif command == 5:
        print(len(testQueue))
    elif command == 6:
        if len(testQueue) != 0:
            print('0')
        else:
            print('1')
    elif command == 7:
        if len(testQueue) != 0:
            print(testQueue[0])
        else:
            print('-1')
    elif command == 8:
        if len(testQueue) != 0:
            print(testQueue[len(testQueue) - 1])
        else:
            print('-1')
