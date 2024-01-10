from collections import deque

def solution(arr):
    answer = []
    length = len(arr)
    for i in range(length):

        # 이미 배열에 원소가 존재하는 경우 끝값과 비교해서 다르면 append 
        if answer and answer[-1] != arr[i]:
            answer.append(arr[i])
        # 만약 answer가 비어있다면 append
        elif not answer:
            answer.append(arr[i])
    return answer

print(solution([1,1,1,3,3,2,4,4,4]))