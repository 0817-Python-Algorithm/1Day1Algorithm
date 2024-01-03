# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    length = len(answers)
    answer_count = [0] * 3 # 수포자들의 정답 개수를 모아둔 배열
    
    # 문제 개수를 고려해서 만든 수포자1 정답리스트
    noMath1 = [1,2,3,4,5] * (length//5 + 1)
    
    for i in range(length):
        if answers[i] == noMath1[i]:
            answer_count[0] += 1
    
    # 문제 개수를 고려해서 만든 수포자2 정답리스트
    noMath2 = [2,1,2,3,2,4,2,5] * (length//8 + 1)
    
    for i in range(length):
        if answers[i] == noMath2[i]:
            answer_count[1] += 1
        
    # 문제 개수를 고려해서 만든 수포자3 정답리스트
    noMath3 = [3,3,1,1,2,2,4,4,5,5] * (length//10 + 1)
    
    for i in range(length):
        if answers[i] == noMath3[i]:
            answer_count[2] += 1
    
    max_answer_count = -1
    answer = []
    
    for i in range(len(answer_count)):

        # 정답 개수가 많은 수포자가 나타날 경우 최대 정답수 갱신, 최대 정답자 list 리셋
        if max_answer_count < answer_count[i]:
            max_answer_count = answer_count[i]
            answer = [i+1]
        
        # 정답 개수가 최대 개수와 동일할 경우 최대 정답자 list에 추가
        elif max_answer_count == answer_count[i]:
            answer.append(i+1)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))


# 정답 패턴을 미리 배열로 만들고 그 길이로 % 연산을 해서 넘치지 않게 활용하는 풀이 방법
def solution2(answers):
    answer_patterns = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer_count = [0] * 3
    max_answer_count = -1
    ans = []
    
    # i for문이 길이가 3이기에 이중 for문이어도 시간 복잡도가 O(N)
    for i in range(3):
        for j, answer in enumerate(answers):
            if answer == answer_patterns[i][j % len(answer_patterns[i])]:
                answer_count[i] += 1
        if max_answer_count < answer_count[i]:
            max_answer_count = answer_count[i]
            ans = [i+1]
        elif max_answer_count == answer_count[i]:
            ans.append(i+1)
    return ans


print(solution2([1,2,3,4,5]))
print(solution2([1,3,2,4,2]))