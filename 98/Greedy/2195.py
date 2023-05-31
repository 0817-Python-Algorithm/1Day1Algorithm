import sys

ip = sys.stdin.readline
S = ip()
P = ip()
start = 0
result = 0
while len(S) !=1:
  for i in range(len(S)):
    if S[0:i] in P:
      continue
    else:
      print(i)
      S = S[i - 1:len(S)]
      result += 1
      break
print("finish")
print(result)