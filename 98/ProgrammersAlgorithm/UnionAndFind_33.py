def find(nodes, x):
    for node in nodes:
        if x in node:
            return node

def union(nodes, x, y):
    find_x = find(nodes, x)
    find_y = find(nodes, y)

    if find_x[0] > find_y[0]:
        find_x += find_y
        nodes.remove(find_y)

    elif find_y[0] > find_x[0]:
        find_y += find_x
        nodes.remove(find_x)
        
def solution(k, operations):
    nodes = list(range(k))
    
    for i in range(k):
        nodes[i] = [i]

    for operation in operations:
        if operation[0] == 'u':
            union(nodes, operation[1], operation[2])
        else:
            find(nodes, operation[1])

    return len(nodes)

print(solution(3, [['u', 0, 1], ['u', 1, 2], ['f', 2]]))
print(solution(4, [['u', 0, 1], ['u', 2, 3], ['f', 0]]))