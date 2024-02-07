def solution(n, times):
    
    max_time = (n // 3 + 1)*max(times)+1
    
    time = [0] * max_time
    
    for i in range(max_time):
        for t in times:
            if i % t == 0:
                time[i] += 1
    
    N = n
    answer = 0
    for index, value in enumerate(time[1:]):
        N -= value
        if N == 0:
            answer = index + 1
            break
    return answer

print(solution(6, [7,10]))
print(solution(5, [7,10,3]))
print(solution(3, [1,99,99]))