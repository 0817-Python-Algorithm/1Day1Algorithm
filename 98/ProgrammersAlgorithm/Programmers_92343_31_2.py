from collections import deque

def solution(info, edges):
  # ➊ 트리 구축 함수
  def build_tree(info, edges):
    tree = [[] for _ in range(len(info))]
    for edge in edges:
      tree[edge[0]].append(edge[1])
    return tree

  tree = build_tree(info, edges)  # ➋ 트리 생성
  max_sheep = 0  # ➌ 최대 양의 수를 저장할 변수 초기화

  # ➍ BFS를 위한 큐 생성 및 초기 상태 설정
  # (현재 위치, 양의 수, 늑대의 수, 방문한 노드 집합)
  q = deque([(0, 1,0, set())])

  # BFS 시작
  while q:
    # ➎ 큐에서 상태 가져오기
    print("q.popleft():", q[0])
    current, sheep_count, wolf_count, visited = q.popleft()
    # ➏ 최대 양의 수 업데이트
    max_sheep = max(max_sheep, sheep_count)
    # ➐ 방문한 노드 집합에 현재 노드의 이웃 노드 추가
    visited.update(tree[current])
    print("visited:", visited)

    # ➑ 인접한 노드들에 대해 탐색
    for next_node in visited:
      if info[next_node]:  # ➒ 늑대일 경우
        if sheep_count != wolf_count + 1:
          q.append(
            (next_node, sheep_count, wolf_count + 1, visited - {next_node})
          )
          print("늑대임, q: ", q)
      else:  # ➓ 양일 경우
        q.append(
          (next_node, sheep_count + 1, wolf_count, visited - {next_node})
        )
        print("양임, q: ", q)
  return max_sheep
                
            

# print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
# print(solution([0,1,0,0,0,1,1,1], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7]]))
print(solution([0,1,0,0,1,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))