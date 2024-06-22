import sys
input = sys.stdin.readline

angle_arr = []
for i in range(3):
    angle_arr.append(int(input()))

if sum(angle_arr) != 180:
    print("Error")
else:
    if len(set(angle_arr)) == 3:
        print("Scalene")
    elif len(set(angle_arr)) == 2:
        print("Isosceles")
    elif len(set(angle_arr)) == 1:
        print("Equilateral")