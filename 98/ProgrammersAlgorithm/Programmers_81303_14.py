
# 해당 index의 행이 최상단인지 여부를 반환
def isTop(arr, index):
    return arr[index][1] == -1

# 해당 index의 행이 최하단인지 여부를 반환
def isBottom(arr, index):
    return arr[index][2] == len(arr)

# number만큼 상단의 index를 반환
def up(arr, current, number):
    for _ in range(number):
        current = arr[current][1]
    return current
        
# number만큼 하단의 index를 반환
def down(arr, current, number):
    for _ in range(number):
        current = arr[current][2]
    return current

# deleted 배열에 삭제할 행의 index값을 push하고 해당 행의 index값을 반환
def delete(arr, deleted, current):
    deleted.append(arr[current][0])
    arr[current][3] = False
    if not isTop(arr, current): #최상단일 경우엔 그보다 상단에 down값을 넘겨줄 수 없으니 예외 처리
        arr[arr[current][1]][2] = arr[current][2]
    if not isBottom(arr, current): #최하단일 경우엔 그보다 gk단에 up값을 넘겨줄 수 없으니 예외 처리
        arr[arr[current][2]][1] = arr[current][1]
    
    # 최하단일 경우엔 그보다 위(up) index를 반환해야 함.
    if isBottom(arr, current):
        return arr[current][1]
    # 아닐 경우, 아래(down) 값을 반환함.
    return arr[current][2]

# deleted 배열에서 복구할 행의 index값을 pop
def restore(arr, deleted):
    index = deleted.pop()
    if not isTop(arr, index): # 최상단일 경우엔 자신의 위(up)값이 없으니 index를 따로 넣어줄 곳이 위로는 없으니 예외 처리
        arr[arr[index][1]][2] = index
    if not isBottom(arr, index): # 최하단일 경우엔 자신의 아래(down)값이 없으니 index를 따로 넣어줄 곳이 아래로는 없으니 예외 처리
       arr[arr[index][2]][1] = index
    arr[index][3] = True

def solution(n, k, cmd):

    current = k
    arr = [[] * 4 for _ in range(n)]
    deleted = []
    
    for i in range(n):
        # arr을 인덱스(int), up값(int), down값(int), exist(boolean)를 갖는다고 생각하여 풀이
        arr[i] = [i, i-1, i+1, True]
    
    for str in cmd:
        command = str.split()
        if command[0] == 'U':
            current = up(arr, current, int(command[1]))
        elif command[0] == 'D':
            current = down(arr, current, int(command[1]))
        elif command[0] == 'C':
            current = delete(arr, deleted, current)
        else:
            restore(arr, deleted)

    answer = ""

    for index in range(len(arr)):
        if arr[index][3]:
            answer += 'O'
        else: 
            answer += 'X'
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))