def solution(n,a,b):
    answer = 0
    
    # 두 숫자가 같아진다는 것은 둘이서 만나서 누군가 이겼다는 뜻임.
    # 이 경우를 생각하면서 한 칸씩 라운드를 진행해보니 쉽게 구할 수 있었음.
    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1

    return answer

print(solution(8,1,7))
print(solution(8,2,7))
print(solution(8,2,3))