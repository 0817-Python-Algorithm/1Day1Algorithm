# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    
    answer = [[0 for i in range(len(arr2[0]))] for i in range(len(arr1))]
    
    # 예를 들어 4X3 * 3*5 이런 방식일 때,
    # 가운데에 오는 3을 calculate_time으로 둠
    calculate_time = len(arr1[0])

    # 단순하게 삼중 for문이기에 시간 복잡도는 O(N^3)
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(calculate_time):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
