def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1
        
def solution(n, costs):

    # 최종비용
    final_cost = 0 
    
    # 현재 사용된 간선의 개수
    count = 0
    
    # 각 노드의 랭크값 배열
    rank = [0] * n

    # 각 노드의 부모노드를 저장한 배열
    parent = [i for i in range(n)]

    # costs를 오름차순으로 정렬
    costs.sort(key = lambda x: x[2])

    for c in costs:
        if count == n - 1:
            break

        parent1 = find(parent, c[0])
        parent2 = find(parent, c[1])
        
        if parent1 != parent2:
            union(parent, rank, parent1, parent2)
            count += 1
            final_cost += c[2]

    
    return final_cost

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))