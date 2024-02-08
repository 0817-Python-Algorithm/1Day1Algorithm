import sys

sys.setrecursionlimit(10**6)

def solution(n, edges):
    
    level = []

    last = [1]
    new_edges = list(edges)
    while new_edges:
        for edge in new_edges:
            if edge[0] in last:
                level.append(edge[1])
            elif edge[1] in last:
                level.append(edge[0])
        new_edges = [edge for edge in new_edges if edge[0] not in last and edge[1] not in last]
        last = level
        level = []
    
    last = [last[-1]]
    depth = 0
    while edges:
        for edge in edges:
            if edge[0] in last:
                level.append(edge[1])
            elif edge[1] in last:
                level.append(edge[0])
        edges = [edge for edge in edges if edge[0] not in last and edge[1] not in last]
        last = level
        level = []
        depth += 1
    if len(last) > 1:
        return depth
    else:
        return depth - 1

# 처음엔 함수 호출량이 많아서 런타임 에러가 뜨는 줄 알아서 재귀 리밋을 늘려줌.
# 하지만 가장 큰 문제는 트리를 만드는 데에도 있었고 지름을 찾는 과정을 2번만 하는 문제에도 있었음.
# 이후 다시 BFS를 활용하여 트리를 만드는 시도를 하게 됨.
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(5, [[1,5],[2,5],[3,5],[4,5]]))
print(solution(11, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [6, 10], [10, 11]]))