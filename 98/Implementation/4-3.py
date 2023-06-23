def inner(a,b):
  if 0<=a and a<=7 and 0<=b and b<=7:
    return True
  else:
    return False

place = input()
x = ord(place[0])-ord('a')
y = int(place[1])-1
result=0
cases = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
for case in cases:
  if inner(x + case[0], y + case[1]):
    result+=1
print(result)
