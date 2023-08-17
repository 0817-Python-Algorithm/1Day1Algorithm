a = input()
count =1
for i in range(1,len(a)):
    if a[i] != a[i-1]:
        count += 1
print(count//2)