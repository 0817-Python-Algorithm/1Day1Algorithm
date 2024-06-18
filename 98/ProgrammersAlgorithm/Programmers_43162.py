def solution(n, computers):
    
    parent = [i for i in range(n)]
    network = {}
    
    index_count = sorted(range(len(computers)), key=lambda x: sum(computers[x]))
    
    for count in index_count:
        for index, c in computers[count]:
            if c == 1:
                parent[]
        if computers[c]

    
    answer = 0
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))