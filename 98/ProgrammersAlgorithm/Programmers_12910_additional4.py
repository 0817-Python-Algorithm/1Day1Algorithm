def solution(arr, divisor):
    arr.sort()
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)

    if not answer:
        answer.append(-1)
    return answer

print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))