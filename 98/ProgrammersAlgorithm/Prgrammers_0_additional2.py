from collections import deque

def solution(s):

    answer = 0
    arr = s.split(" ")
    length = len(arr)
    
    for i in range(length):
        # Z일 경우 앞에서 더했던 값을 다시 뺌
        if arr[i] == "Z":
            answer -= int(arr[i-1])
        # 숫자일 경우엔 그대로 더해줌
        else:
            answer += int(arr[i])
            
    return answer

print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))