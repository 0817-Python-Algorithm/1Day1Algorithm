import sys
input = sys.stdin.readline().rstrip().split(" ")

nums = list(map(int,input))
x = nums[0]
y = nums[1]
w = nums[2]
h = nums[3]

distances = [x, y, w-x, h-y]
answer = 1000
for i in distances:
    if answer > i:
        answer = i
print(answer)
