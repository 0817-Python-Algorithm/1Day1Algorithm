import sys
input = sys.stdin.readline

def findAnother(arr):
    if arr[0] == arr[1]:
        return arr[2]
    elif arr[0] == arr[2]:
        return arr[1]
    else:
        return arr[0]
    
x = []
y = []
for i in range(3):
    coordinate = list(map(int, input().split(" ")))
    x.append(coordinate[0])
    y.append(coordinate[1])
print(findAnother(x), findAnother(y))