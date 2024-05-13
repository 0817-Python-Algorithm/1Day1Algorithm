number = input()
N = [int(c) for c in number]
N.sort(reverse = True)
for i in N:
    print(i, end = "")
    