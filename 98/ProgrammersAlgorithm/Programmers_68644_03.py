# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    newSet = set()
    length = len(numbers)
    
    # 이 이중 for문으로 인해 시간 복잡도는 O(N^2)
    for i in range(length-1):
        for j in range(i+1, length):
            newSet.add(numbers[i]+numbers[j])
    newList = list(newSet)
    
    # N^2을 짜리를 정령하니 시간 복잡도는 O(N^2log(N^2))
    newList.sort()
    answer = newList
    return answer
