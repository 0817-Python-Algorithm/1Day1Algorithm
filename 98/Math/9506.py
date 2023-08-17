import sys

while True:
    N = int(sys.stdin.readline())
    if N == -1:
        exit()
    total = 1
    result = str(N) + " = 1"
    for i in range(2, N):
        if N % i == 0:
            total += i
            result += " + " + str(i)
    if total == N:
        print(result)
    else:
        print(str(N)+" is NOT perfect.")
