def solution(enroll, referral, seller, amount):
    route = {"-": []}
    revenue = {"-": 0}
    
    N = len(enroll)
    S = len(seller)
    
    for i in range(N):
        route[enroll[i]] = [referral[i]] + (route[referral[i]])
        revenue[enroll[i]] = 0
    
    for i in range(S):
        person =  seller[i]
        primary =  route[person]
        money = amount[i] * 100

        for j in [person]+primary:
            # 중간에 테스트가 시간초과가 떴었는데 money < 10일 경우엔 그냥 자기가 다 갖고 위에 줄 필요가 없으므로 이때도 break해야함.
            # 위로 계속 0을 넘겨줄 경우 의미없는 행위가 반복될 수 있기 때문임.
            if j == "-" or money < 10:
                revenue[j] += money
                break
            revenue[j] += (money - money//10)
            money = money // 10
    
    answer = []
    for r in revenue.values():
        answer.append(r)
    return answer[1:]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))