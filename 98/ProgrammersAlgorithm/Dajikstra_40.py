from collections import deque

def solution(graph, start):

    length = len(graph)
    INF = 10000
    visit = set()
    route = {node: [start] for node in graph}
    amount = {node: INF for node in graph} # 이렇게 작성하는 법을 잊지 말자.
    queue = deque()
    amount[start] = 0
    queue.append(start)
    while queue:
        location = queue.popleft()
        visit.add(location)
        for key, value in graph[location].items():
            if amount[key] > amount[location] + value:
                amount[key] = amount[location] + value
                route[key] = route[location]+[key]
        filtered_items = dict((key, value) for key, value in amount.items() if key not in visit)
        if filtered_items:  # 방문하지 않은 노드가 남아있는 경우에만 처리
            min_node = min(filtered_items, key=filtered_items.get) # 이런 방식으로 하면 value값이 최소인 key를 구하는 것임.
            queue.append(min_node)

    return [amount, route]


print(solution({'A': {'B':9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1}},'A'))
print(solution({'A': {'B':1}, 'B': {'C': 5}, 'C': {'D': 1}, 'D': {}},'A'))