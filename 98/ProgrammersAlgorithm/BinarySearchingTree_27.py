# Node 클래스
class Node:
    def __init__(self, key):
        # Node의 왼쪽에 빈 값(추후 노드를 둘 예정)
        self.left = None
        # Node의 오른쪽에 빈 값(추후 노드를 둘 예정)
        self.right = None
        # Node 자체가 가지는 값(val)
        self.val = key

class BST:
    # 이진 탐색 트리의 루트를 빈 값으로 초기화 해 둠(추후 노드를 둘 예정)
    def __init__(self):
        self.root = None
    
    # 이진 탐색 트리에 값을 추가해 넣는 함수
    def insert(self, key):
        # 만약 루트가 비어있다면 해당 key값을 val로 갖는 Node를 루트로 둠.
        if not self.root:
            self.root = Node(key)
        # 만약 루트가 존재한다면
        else:
            # 편하게 이름을 current로 두고,
            current = self.root
            
            while True:
                # current의 값보다 key가 작다면
                if key < current.val:
                    # 만약 current가 왼쪽 노드가 있다면 그걸 current로 설정해두고 계속 탐색
                    if current.left:
                        current = current.left
                    # 만약 current가 왼쪽 노드가 없다면 해당 key값을 val로 갖는 Node를 current의 left로 설정한 뒤 끝냄.
                    else:
                        current.left = Node(key)
                        break
                # current의 값보다 key가 크다면
                elif key > current.val:
                    # 만약 current가 오른쪽 노드가 있다면 그걸 current로 설정해두고 계속 탐색
                    if current.right:
                        current = current.right
                    # 만약 current가 오른쪽 노드가 없다면 해당 key값을 val로 갖는 Node를 current의 right로 설정한 뒤 끝냄.
                    else:
                        current.right = Node(key)
                        break
    # 주어진 key값이 현재 이진 트리에 존재하는지 확인하고 있으면 해당 Node를, 없다면 None을 return하는 함수
    def search(self, key):
        # 일단 기본적으로 self.root를 current란 이름으로 간단하게 바꾸고,
        current = self.root
        
        # 만약 current가 없거나(찾는 key값이 이진 트리에 없다는 의미) 해당 current의 val과 주어진 key값이 같다면 current를 리턴함.
        # 이때 전자는 None이, 후자는 Node 객체가 return 될 것임.
        while current and current.val != key:
            # current가 None이 아니지만 val값이랑 key값이 같지 않기에 해당 Node(current)의 left,right를 뒤져야 함.
            # 그래서 key가 val보다 작으면 current를 left로 바꿔주는 거고, 크면 right로 바꿔주는 것임.
            if current.val > key:
                current = current.left
            else:
                current = current.right

        return current

def solution(lst, search_lst):
    # 이진 탐색 트리를 초기화.
    bst = BST()
    
    # 이진 탐색 트리에 값들을 넣어주는 과정
    for i in lst:
        bst.insert(i)

    answer = []
    
    # search_lst에 있는 값들이 있는지 검사하는 과정
    for i in search_lst:
        if bst.search(i):
            answer.append(True)
        else:
            answer.append(False)

    return answer

print(solution([5,3,8,4,2,1,7,10], [1,2,5,6]))
print(solution([1,3,5,7,9], [2,4,6,8,10]))