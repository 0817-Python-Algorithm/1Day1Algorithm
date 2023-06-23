import sys

count = 0
n = int(sys.stdin.readline())
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in "{:02}{:02}{:02}".format(i,j,k):
                count+=1
print(count)