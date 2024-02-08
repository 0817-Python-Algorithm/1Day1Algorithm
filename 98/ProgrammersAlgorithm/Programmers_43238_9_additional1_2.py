# 시간 복잡도는 O(M)임.
def calculate(n, times, number):
    count = 0
    for t in times:
        count += number // t
    return count

def solution(n, times):
    left = 0

    # n의 최대값 10**9와 times의 요소의 최대값 10**9를 곱한 값을 가능한 최대로 두고 풀음.
    right = 10**18
    
    # 이진 탐색이므로 시간 복잡도는 O(logN)임.
    while True:
        mid = (left + right) // 2
        count = calculate(n,times, mid)
        
        # n == count 시에 mid를 left가 아닌 right에 넣어주는 이유는 mid 계산 시 .5를 버리게 되므로 좌측에 쏠리게 되는 현상이 있으므로
        if n <= count:
            right = mid
        else:
            left = mid
        
        # 다 좁혀졌으면 둘 중 올바른 것을 가지고 return.
        # 우선적으로 left가 작으니 left 먼저 확인하고 그 다음에 right를 판단함.
        if right - left <= 1:
            if calculate(n, times, left) == n:
                return left
            else:
                return right

print(solution(6, [7,10]))
print(solution(5, [7,10,3]))
print(solution(3, [1,99,99]))
print(solution(1, [1,99,1000000000]))