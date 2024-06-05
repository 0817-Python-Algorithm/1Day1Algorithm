import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))

site_password = dict()

for i in range(N):
    info = input().rstrip().split(" ")
    site_password[info[0]] = info[1]

for i in range(M):
    print(site_password[input().rstrip()])