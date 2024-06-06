import sys
input = sys.stdin.readline

n = int(input())

entrance = set()

for i in range(n):
    record = input().rstrip().split(" ")

    if record[1] == "enter":
        entrance.add(record[0])
    elif record[1] == "leave":
        entrance.remove(record[0])

entrance_arr = list(entrance)
entrance_arr.sort(reverse = True)

for name in entrance_arr:
    print(name)