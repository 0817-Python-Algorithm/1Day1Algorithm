from collections import defaultdict

def solution(graph, start):
    linked_list = defaultdict(list)
    
    for e, v in graph:
        linked_list[e].append(v)
    
    visited = set()
    stack = []
    result = []
    
    def dfs(node, visited, stack):
        visited.add(node)
        result.append(node)
        for l in linked_list[node]:
            if l not in visited:
                dfs(l, visited, stack)

    dfs(start, visited, stack)
    return result

print(solution([['A','B'],['B','C'],['C','D'],['D','E']],'A'))
print(solution([['A','B'],['A','C'],['B','D'],['B','E'],['C','F'],['E','F']],'A'))
