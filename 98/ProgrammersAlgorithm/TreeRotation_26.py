# 전위 순회
def preorder(nodes, idx):
    if idx < len(nodes):
        result = str(nodes[idx])+" "
        result += preorder(nodes, idx*2+1)
        result += preorder(nodes, idx*2+2)
        return result
    else:
        return ""
# 중위 순회
def inorder(nodes, idx):
    if idx < len(nodes):
        result = inorder(nodes, idx*2+1)
        result += str(nodes[idx]) + " "
        result += inorder(nodes, idx*2+2)
        return result
    else:
        return ""
# 후위 순회
def postorder(nodes, idx):
    if idx < len(nodes):
        result = postorder(nodes, idx*2+1)
        result += postorder(nodes, idx*2+2)
        result += str(nodes[idx]) + " "
        return result
    else:
        return ""


def solution(nodes):
    # [:-1]을 하는 이유: 순회한 결과 마지막에 " "이 하나 들어가게 되는데 그걸 잘라주는 스킬임.
    answer = [preorder(nodes, 0)[:-1], inorder(nodes, 0)[:-1], postorder(nodes, 0)[:-1]]
    return answer

print(solution([1,2,3,4,5,6,7]))