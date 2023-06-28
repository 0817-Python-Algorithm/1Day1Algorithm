def d(n):
    res = n
    while(n!=0):
        res += n%10
        n //= 10
    return res
arr = [0] * 10001
for i in range(1, 10001):
    a = d(i)
    if a<10001:
        arr[a] = 1
for i in range(1,10001):
    if arr[i]==0:
        print(i)
