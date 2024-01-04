def is_valid_location(nx, ny):
    if 0 <= nx < 11 and 0 <= ny < 11:
        return True
    return False

def move_location(x, y, dir):

    nx, ny = 0, 0
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'L':
        nx, ny = x-1, y
    elif dir == 'R':
        nx, ny = x+1, y

    if is_valid_location(nx, ny):
        return nx, ny
    else:
        return x, y

def solution(dirs):

    # 중복인 걸 거를 때는 set을 항상 생각해보는게 좋음!
    move_set = set()
    x, y = 5, 5
    for dir in dirs: # python에서는 String을 for문 돌리면 한 글자씩 받아올 수 있음.
        nx, ny = move_location(x, y, dir)
        if x != nx or y != ny:
            move_set.add((x, y, nx, ny))
            move_set.add((nx, ny, x, y))
            
            x, y = nx, ny
        
    answer = len(move_set) // 2 
    return answer

print(solution("ULURRDLLU"))