def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
    
def top(stack):
    if len(stack) == 0:
        return -1
    return len(stack) - 1

def push(stack, item):
    return stack.append(item)

def pop(stack):
    return stack.pop()

def solution(s):

    answer = 0 # 정답 개수
    arr = [] # 받아온 문자열을 배열 형태로 변환
    stack = [] # 문제 풀이에서 넣었다 뺐다 할 배열
    length = len(s)

    # 문자열을 배열로 변환
    for str in s:
        arr.append(str)

    # 배열 자체를 새로 돌릴 생각을 하지말고 시작하는 index int값을 바꿔가면서 %length를 활용하기
    for start_index in range(length):
        stack = []
        for index in range(length):
            if arr[(index+start_index)%length] == '(' or arr[(index+start_index)%length] == '{' or arr[(index+start_index)%length] == '[':
                push(stack, arr[(index+start_index)%length])
            elif isEmpty(stack):
                break
            elif arr[(index+start_index)%length] == ')' and stack[top(stack)] == '(':
                pop(stack)
            elif arr[(index+start_index)%length] == '}' and stack[top(stack)] == '{':
                pop(stack)
            elif arr[(index+start_index)%length] == ']' and stack[top(stack)] == '[':
                pop(stack)
            else:
                break
            if index == length - 1 and isEmpty(stack):
                answer += 1
        
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))