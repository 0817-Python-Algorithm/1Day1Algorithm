def solution(decimal):
    stack = []
    while True:
        if decimal == 0:
            break
        if decimal % 2 == 1:
            stack.append("1")
        else:
            stack.append("0")
        decimal = decimal // 2
    stack.reverse()
    return ''.join(stack)

print(solution(10))
print(solution(27))
print(solution(12345))