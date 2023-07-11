N = input()
count = [0] * 10
for i in N:
    i = int(i)
    if i == 9 or i ==6:
        if count[6] < count[9]:
            i=6
        else:
            i=9
    
    count[i] += 1
count[6] = round(count[6]/2)
print(max(count))