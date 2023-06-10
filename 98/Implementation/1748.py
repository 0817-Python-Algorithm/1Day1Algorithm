import sys
n = sys.stdin.readline().rstrip()
result = 0
for i in range(0, len(n)-1):
  result+=9*(10**i)*(i+1)
result+=(int(n)%(10**(len(n)-1))+1)*len(n)
print(result)