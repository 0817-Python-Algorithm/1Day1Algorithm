a, b = map(int, input().split())
result = 0
while True:
  if a%b ==0:
    a = a/b
  else:
    a = a - 1
  result +=1
  if a == 1: break
print(result)