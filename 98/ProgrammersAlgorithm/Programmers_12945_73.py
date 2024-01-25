def solution(n):
    fibonacci = [0,1]
    for i in range(2,n+1):
        # 숫자가 커질 수 있기에 미리 중간 중간 모듈러 연산 처리함.
        # 이건 모듈러 연산을 참고하면 됨.
        fibonacci.append((fibonacci[i-2]%1234567 + fibonacci[i-1]%1234567)%1234567)
    
    answer = fibonacci[n]
    return answer

print(solution(3))
print(solution(5))
print(solution(10))