def solution(n, left, right):
    answer = []
    for index in range(left, right+1):
        # 직접 배열을 만들고 값을 넣는 방식 대신에 해당 index의 행, 열이 이미 그 안에 들어갈 값을 알고있다고 생각함.
        # 계산을 하다보니 index의 몫과 나머지 중 큰값 + 1이 index의 값이 된다는 사실을 발견함.
        # 다중 for문을 단일 for문으로 구현해낼 수 있게 됨.
        # index 자체가 어떤 역할을 할 수 있는지도 잘 활용하면 코드를 간결하게 바꿀 수 있다는 것을 느낌.
        answer.append(max(index//n, index%n)+1)
    return answer

print(solution(4, 7, 14))