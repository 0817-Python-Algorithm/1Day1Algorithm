def solution(n, times):
    i = 0
    time = 0
    while True:
        i += 1
        for t in times:
            if i % t == 0:
                time += 1
            if time == n:
                return i

# 너무 단순하게 풀려고 했음. 이 경우 순차탐색이기에 최대 O(N*M)이 나올 수 있음.
# 이러한 과도한 계산을 방지하고자 탐색을 순차탐색 대신 이진탐색을 사용하는 것이 좋음.

print(solution(6, [7,10]))
print(solution(5, [7,10,3]))
print(solution(3, [1,99,99]))
print(solution(1, [1,99,1000000000]))