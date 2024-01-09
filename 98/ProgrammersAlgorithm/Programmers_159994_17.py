from collections import deque

def solution(cards1, cards2, goal):
    queue1 = deque(cards1) # cards1 deque 변환에 O(N)
    queue2 = deque(cards2) # cards2 deque 변환에 O(N)
    
    # goal을 돌면서 만약 조건을 만족하면서 해당 골과 같은 값을 가진 큐가 없다면 바로 retrun 'No'
    for goal_word in goal: # for 문 순환에 O(M)
        # 주의: 아래처럼 항상 queue1을 먼저 검사하고 queue2를 검사해도 문제가 없는 이유는 겹치는 단어가 하나도 없기에 가능한 것임.

        # 만약 queue1의 길이가 0이 아니고 goal과 동일한 값이 맨 앞에 존재한다면 pop
        if queue1 and queue1[0] == goal_word:
            queue1.popleft()
        # 만약 queue2의 길이가 0이 아니고 goal과 동일한 값이 맨 앞에 존재한다면 pop
        elif queue2 and queue2[0] == goal_word:
            queue2.popleft()
        else:
            return 'No'
    return 'Yes'

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

# 이런 반례를 생각했는데 잘 읽어보니,
# "cards1과 cards2에는 서로 다른 단어만 존재합니다." 라는 조건이 존재하기에 배제했다.
print(solution(["A", "A", "B"], ["A", "C"], ["A", "D", "C", "A", "B"])) 