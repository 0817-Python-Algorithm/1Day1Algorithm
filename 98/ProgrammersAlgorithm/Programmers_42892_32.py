# 이게 사실상 이 문제의 핵심 포인트이지 않을까 싶음.
# 재귀로 문제를 풀 경우 함수를 호출하는 최대 limit이 1000에 가깝기에 이 부분에서 이슈가 발생할 수 있음.
# 강제로 sys 자체에석 limit을 높여주면 해결이 됨.
# 참고 자료에선 10**6으로 했지만 사실 10**4 정도로만 늘려줘도 굴러감.
# 참고 링크: https://school.programmers.co.kr/questions/3723
import sys
sys.setrecursionlimit(10000)

# Node 클래스
class Node:
    def __init__(self, parent, childs):
        self.location = parent
        self.left = None
        self.right = None

        temp = self.make_tree(parent, childs)
        
        if len(temp[0]) >= 1:
            self.left = Node(temp[0][0], temp[0][1:])

        if len(temp[1]) >= 1:
            self.right = Node(temp[1][0], temp[1][1:])
    
    # 주어진 parent를 기준으로 childs 좌우로 나누어 tree 재료를 만드는 함수
    def make_tree(self, parent, childs):
        temp_left = []
        temp_right = []
        for c in childs:
            if c[0] < parent[0]:
                temp_left.append(c)
            else:
                temp_right.append(c)
        return [temp_left, temp_right]

# 주어진 노드를 가지고 하단 트리를 전위 순회하는 함수 
def make_preorder(root):
    order = []

    order.append(root.location[2])

    if root.left is not None:
        order += make_preorder(root.left)

    if root.right is not None:
        order += make_preorder(root.right)

    return order

# 주어진 노드를 가지고 하단 트리를 후위 순회하는 함수
def make_postorder(root):
    order = []

    if root.left is not None:
        order += make_postorder(root.left)

    if root.right is not None:
        order += make_postorder(root.right)

    order.append(root.location[2])

    return order

def solution(nodeinfo):
    new_nodeinfo = []
    
    # 각 좌표에 index값을 합치는 과정
    for i in range(len(nodeinfo)):
        new_nodeinfo.append(nodeinfo[i]+[i+1])

    # 주어진 nodeinfo를 가지고 y좌표 내림차순으로 만드는 과정
    new_nodeinfo = sorted(new_nodeinfo, key = lambda x: x[1], reverse = True)

    root = Node(new_nodeinfo[0], new_nodeinfo[1:])

    preorder = make_preorder(root)
    postorder = make_postorder(root)

    answer = [preorder, postorder]
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
print(solution([[5,2]]))
print(solution([[5,2],[6,1]]))