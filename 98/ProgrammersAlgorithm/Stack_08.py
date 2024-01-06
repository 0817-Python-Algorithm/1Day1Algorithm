def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def top(stack):
    return stack[len(stack) - 1]

def push(stack, item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        print("스택이 비어있습니다.")
    else:
        return stack.pop()
        
def solution(str):
    stack  = []
    
    for s in str:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if isEmpty(stack):
                return False
            pop(stack)
    if isEmpty(stack):
        return True
    else: 
        return False

print(solution("(())()"))
print(solution("((())()"))