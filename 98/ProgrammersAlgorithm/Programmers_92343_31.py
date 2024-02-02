from collections import deque
        

def solution(info, edges):
    visit = [False]*len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for edge in edges:
            if visit[edge[0]] and not visit[edge[1]]:
                visit[edge[1]] = True
                if info[edge[1]] == 1:
                    dfs(sheep, wolf+1)
                else:
                    dfs(sheep+1, wolf)
                visit[edge[1]] = False
    visit[0] = True
    dfs(1,0)

    return max(answer)
                
# 이 문제를 푸는 방법에는 여러가지가 있음.
# 일단 기본적으로는 너비우선탐색(BFS)으로 찾을 수 있는데 솔직히 말해서 이 풀이 방식을 생각해내기 어려울 것 같음.
# 개념은 알아도 이 문제에 적용해서 푸는 데에 살짝 한계를 느낌.
# 그래서 그나마 쉬운 깊이우선탐색(DFS)으로 풀었음.
# 생각보다 코드가 짧기도 했고 그렇게 크게 오래 걸리는 문제도 아니기에 오히려 DFS방식도 괜찮은 방식이라고 생각이 되었음.

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,0,1], [[0,1],[0,2],[1,3],[2,4]]))