S = input()
P = input()
start = 0
result = 0
while len(P) != 0:
    if P in S:
        result += 1
        break
    for i in range(len(P)):
        if (P[0:i+1] in S) and not (P[0:i+2] in S):
            result += 1
            P = P[i+1:]
            break
print(result)