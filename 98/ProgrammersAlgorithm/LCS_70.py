def solution(str1, str2):

    len1 = len(str1)
    len2 = len(str2)
    
    # 일단 테이블을 만듦
    table = [[0]*len2 for i in range(len1)]
    
    # (0,0),(0,1),(1,0)에는 미리 값을 넣어둠.
    if str1[0] == str2[0]:
        table[0][0] = 1

    if len2 > 1:
        if str1[0] == str2[1]:
            table[0][1] = 1
        else:
            table[0][1] = table[0][0]

    if len1 > 1:
        if str1[1] == str2[0]:
            table[1][0] = 1
        else:
            table[1][0] = table[0][0]
    
    # 비교하면서 값을 넣음
    for i in range(1,len1):
        for j in range(1,len2):
            # 만약 두 문자열에서 1개씩 추가했는데 그게 같다면 이전 상태의 결과에서 1을 더함      
            if str1[i] == str2[j]:
                table[i][j] = table[i-1][j-1] + 1
            # 다르다면 두 문자열 중 1개씩만 추가 시 어떤게 큰지 비교하고 그것으로 값을 대체함
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    return table[len1-1][len2-1]


print(solution("ABCBDAB", "BDCAB"))
print(solution("AGGTAB", "GXTXAYB"))