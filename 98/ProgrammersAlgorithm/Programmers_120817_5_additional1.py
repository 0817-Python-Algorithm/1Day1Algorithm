def solution(numbers):
    total = 0
    
    for number in numbers:
        total += number

    answer = total / len(numbers)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))