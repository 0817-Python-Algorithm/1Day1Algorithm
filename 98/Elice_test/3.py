import sys
input = sys.stdin.readline

word = input().rstrip()
stack = list(word)

result = 0

while True:
    if stack[-1] == ')':
        stack.pop()
    elif stack[-1] == '(':
        stack.pop()
        result *= int(stack.pop())
    else:
        result += 1
        stack.pop()
    if len(stack) == 0:
        break
print(result)
