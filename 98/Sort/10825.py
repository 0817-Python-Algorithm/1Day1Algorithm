
import sys
from functools import cmp_to_key

N = int(input())
names = [''] * N
scores = [[0,0,0,0]] * N

def compare(a,b):
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    else:
        if a[1] < b[1]:
            return -1
        elif a[1] > b[1]:
            return 1
        else:
            if a[2] > b[2]:
                return -1
            elif a[2] < b[2]:
                return 1
            else:
                if names[a[3]] < names[b[3]]:
                    return -1
                else:
                    return 1
                 

for i in range(N):
    information = sys.stdin.readline().rstrip().split(" ")
    names[i] = information[0]
    scores[i] = [int(i) for i in information[1:4]+[i]]

scores.sort(key = cmp_to_key(compare))

for i in range(N):
    print(names[scores[i][3]])