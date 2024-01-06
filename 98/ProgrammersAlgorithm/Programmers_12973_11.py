def isEmpty(stack):
    return len(stack) == 0

def solution(s):

    stack = [s[0]] # 일단 첫 데이터는 넣고,
    length = len(s)

    
    for i in range(1, length):

        # 앞에 남아있는게 있다면,
        if len(stack) != 0:
            # 끝자리가 넣으려는 것과 동일하다면 삭제함.
            if stack[-1] == s[i]:
                stack.pop()
            # 동일하지 않다면 추가함.
            else:
                stack.append(s[i])
        # 앞에 남아있는게 없다면 추가함.
        else:
            stack.append(s[i])
    if isEmpty(stack):
        answer = 1
    else:
        answer = 0

    return answer

print(solution('aabbddc'))
print(solution('aabbdd'))