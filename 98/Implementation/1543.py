import sys

doc = sys.stdin.readline()
search = sys.stdin.readline()
result = 0
index = 0
while index <= len(doc)-len(search):
    if doc[index: index + len(search)] == search:
      index += len(search)
      result += 1
    else:
      index += 1
print(result)
