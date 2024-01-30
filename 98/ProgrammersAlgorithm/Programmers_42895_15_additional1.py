def solution(N, number):
    
    dp = [set([]) for _ in range(9)]
    # 일단 해당 풀이는 기본적으로 각 숫자마다 사칙연산을 갖도록 하기 때문에 5, 55, 555, ...와 같은 값을 가질 수 없는 형태임.
    # 그래서 미리 조합해서 32000 아래의 값이 나올 수 있을 것이라고 생각되는 6자리 숫자까지 넣어줌.(사실 4까지만 해도 문제는 없음.)
    # 하지만 어차피 6자리까지 해도 최대로 곱해서 나오는 결과 값이 1억을 못넘기는 형태기에 오버플로우 문제는 없음.
    dp[1].add(N*1)
    dp[2].add(N*11)
    dp[3].add(N*111)
    dp[4].add(N*1111)
    # dp[5].add(N*11111)
    # dp[6].add(N*111111)
    for i in range(2, 9):
        temp = set()
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    
                    temp.update([k+l, k-l, k*l, l-k])
                    if k !=0:
                        temp.add(l//k)
                    if l !=0:
                        temp.add(k//l)
        dp[i].update(temp)
    for i in range(1,9):
        if number in dp[i]:
            return i
    answer = -1
    return answer

print(solution(5, 12))
print(solution(2, 11))
print(solution(1, 11))
print(solution(1, 88))
print(solution(1, 121))