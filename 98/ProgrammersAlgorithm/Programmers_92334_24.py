def solution(id_list, report, k):
    
    # 나를 신고한 사람의 명단을 생성
    my_reporter_table = {}

    # report의 길이만큼이라 시간 복잡도는 O(N)
    for r in report:
        info = r.split(" ")
        if info[1] in my_reporter_table:
            my_reporter_table[info[1]].add(info[0])
        else:
            my_reporter_table[info[1]] = set([info[0]])
    
    # 신고가 k번 이상이어서 신고 결과가 될 대상들 명단 생성
    # 신고자 명단은 아무리 길어도 1000
    reported_table = []
    for key, reporters in my_reporter_table.items():
        if len(reporters) >= k:
            reported_table.append(key)

    # 신고 메일을 받아볼 사람이 받을 메일 개수 테이블 초기화
    # id_list는 길이가 아무리 길어도 1000
    result = {}
    for user in id_list:
        result[user] = 0

    # 피신고자를 신고한 사람들의 value값들을 1씩 증가.
    # 신고가 k번 이상인 명단은 아무리 길어도 1000이고, 그 안에서 나를 신고한 사람은 아무리 많아도 1000이기에 의미있는 시간복잡도는 아님.
    for r in reported_table:
        for p in my_reporter_table[r]:
            result[p] += 1
                
    answer = []
    
    # 신고자 명단 내 신고횟수를 id_list 순서대로 출력
    # id_list는 아무리 길어도 1000
    for user in id_list:
        answer.append(result[user])
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))