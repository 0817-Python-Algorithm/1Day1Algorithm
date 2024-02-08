from collections import defaultdict, deque

# BFS를 통해 트리를 생성하는 속도를 O(N)으로 높여줌.
def dfs(start, link, n):
    visited = [False]*(n+1)
    visited[start] = True
    queue = deque([(start, 0)])
    temp_level = 0
    count = 0

    while queue:
        node, level = queue.popleft()
        if temp_level == level:
            count += 1
        else:
            count = 1
            temp_level = level
        visited[node] = True
        for i in link[node]:
            if not visited[i]:
                queue.append((i, level+1))
        if len(queue) == 0:
            return (node, level, count)

# 이 문제에서 얻어갈 콜렉션 타입은 defaultdict임.
# 이 dictionary를 가지고 사용할 경우 어떤 key가 없어도 따로 if문을 작성할 필요없이 바로 append해주면 key-value 관계가 형성됨.
def solution(n, edges):
    link = defaultdict(list)
    for x, y in edges:
        link[x].append(y)
        link[y].append(x)
    
    first_time = dfs(1, link, n)
    # 처음 걸 해준 후 두번째 꺼를 해주면 트리의 원 위의 하나를 구할 수 있음. 하지만 이것을 통해서 여러개가 있다는 것을 완전히 입증하기가 어려움.
    # 참조: https://rkdxowhd98.tistory.com/201
    # 그래서 second_time이 아닌 third_time까지 가줘야 함.
    second_time = dfs(first_time[0], link, n)
    
    # third_time을 가주지 않으면 4,24,25,26번 테스트 케이스에서 문제가 생김.
    # 이때 중요한 것은 반드시 third_time의 결과물을 사용하는 것이 아닌 second_time의 결과물에서 n > 2(즉, 트리의 지름이 두개 이상인 경우)를 고려해야 함.
    # 그래서 둘 중 하나라도 1보다 크면 지름을 리턴하도록 하는 것임.
    # 이 부분 때문에 12번 테스트 케이스에서 틀렸었음.
    third_time = dfs(second_time[0], link, n)
    if third_time[2] > 1 or second_time[2] > 1:
        return third_time[1]
    else:
        return second_time[1] - 1


print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(5, [[1,5],[2,5],[3,5],[4,5]]))
print(solution(11, [[1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8], [8,9], [6,10], [10,11]]))
print(solution(3, [[1,2], [2,3]]))