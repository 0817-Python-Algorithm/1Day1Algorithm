A,B = map(int, input().split())
count = 1
while(A < B):
    count += 1
    bstr = str(B)
    if bstr[-1] == '1':
        bstr = bstr[:-1]
        B = int(bstr)
    elif B%2 == 0:
        B = B//2
    else:
        break
if A==B:
    print(count)
else:
    print(-1)