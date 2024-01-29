def solution(N, number):
    
    dp = [set([]) for _ in range(9)]
    dp[1].add(N*1)
    dp[2].add(N*11)
    dp[3].add(N*111)
    dp[4].add(N*1111)
    dp[5].add(N*11111)
    dp[6].add(N*111111)
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
                    if 88 in temp:
                        print(i,j,k,l)
                        return
        dp[i].update(temp)
    for i in range(1,9):
        if number in dp[i]:
            return i
    answer = -1
    return answer

# print(solution(5, 12))
# print(solution(2, 11))
# print(solution(1, 11))
print(solution(1, 88))
# print(solution(1, 121))