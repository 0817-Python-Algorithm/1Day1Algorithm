from itertools import combinations

def solution(orders, course):
    answer = []

    # course를 순회하면서 해당 길이 기준 가장 많이 시킨 메뉴를 뽑아낼 것임.
    for c in course:
        set_candidate = {} # ex) {"AC": 3, "AE": 5}
        max_length = 0

        # orders를 순회하면서 뽑혀진 그 길이로 조합을 만들고 set_candidate에 등장횟수 1 증가
        for order in orders:

            # sort를 해야 순서가 달라서 combi로 생성안되는 경우 방지 가능
            # ex) "VWX", "XWY"이면 WX, XW를 다르다고 판단하게 되므로 순서를 맞춰줘야 함.
            for combi in combinations(sorted(order), c):
                combi_str = ""
                combi_str += "".join(combi)

                if combi_str in set_candidate:
                    set_candidate[combi_str] += 1
                else:
                    set_candidate[combi_str] = 1
                
                # max_length가 업데이트될 수 있는지 확인
                if set_candidate[combi_str] > max_length:
                    max_length = set_candidate[combi_str]
        
        # 동일한 길이의 후보들 중에 등장횟수가 가장 큰 애들만 더해줘야 함 + 등장횟수도 2회 이상을 만족해야 함.
        for key in set_candidate.keys():
            if set_candidate[key] == max_length and max_length >= 2:
                answer.append(key)
    
    # 결과를 사전식으로 오름차순으로 출력해야 하기 때문에 sort를 함.
    answer = sorted(answer)
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))