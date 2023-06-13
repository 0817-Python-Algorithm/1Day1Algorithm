import sys
n = int(sys.stdin.readline().rstrip())
standard = list(map(int, sys.stdin.readline().rstrip().split()))
comparison = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0
start = standard.index(comparison[0])
arr1 = standard[start:]+standard[:start]
standard2 = standard[::-1]
start = standard2.index(comparison[0])
arr2 = standard2[start:]+standard2[:start]

if arr1 == comparison or arr2 == comparison:
    print("good puzzle")
else:
    print("bad puzzle")




