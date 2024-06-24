import sys

input = sys.stdin.readline

tempData = [0]*5
totalTime = 0
isFrozen = False

for i in range(5):
    tempData[i] = int(input())
if tempData[0] < 0:
    isFrozen = True


while tempData[0] != tempData[1]:
    if tempData[0] < 0:
        totalTime += tempData[2]
        tempData[0] += 1
    elif tempData[0] == 0 and isFrozen == True:
        totalTime += tempData[3]
        isFrozen = False
    else:
        totalTime += tempData[4]
        tempData[0] += 1
print(totalTime)