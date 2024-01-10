def solution(s):
    
    stack = []
    for c in s:
        # ( 인 경우엔 그냥 append해줌
        if c == "(":
            stack.append("(")
        # 만약 stack이 비어있거나 끝값이 (가 아닌 상태에서 )가 나온 거면 바로 실패(False)를 반환
        elif not stack or stack[-1] != "(":
            return False
        # 나머지의 경우는 (를 )로 상쇄시키는 경우이므로 pop
        else:
            stack.pop()
    # 만약 stack이 깔끔하게 비워졌다면 True르 반환
    if not stack:
        return True
    # 아니라면 불완전한 괄호 형태이므로 False를 반환
    else:
        return False

print(solution("()"))
print(solution(")()("))
print(solution("())()"))
print(solution("((())())()"))
