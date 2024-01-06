
# 이 문제를 풀면서 가장 key point는 prices의 최대 길이가 10만이라서 O(N)이 적합하다는 점임.
# 계속해서 증가할 경우엔 
def solution(prices):
    l = len(prices)
    answer = list(map(lambda x: l-1-x, range(0, l)))
    stack = [0]
    for i in range(1, l):
        if stack and prices[i - 1] > prices[i]:
            answer[i - 1] = 1
            stack.pop()
            while True and stack: # stack이라고만 하면 if문에서 stack 리스트가 비어있으면 false, 아니면 True로 동작함.
                if prices[stack[-1]] > prices[i]:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                else: 
                    break
            stack.append(i)
        else:
            stack.append(i)
    
    return answer

print(solution([3,2,3,2,3]))
print(solution([3,3,3,3,3]))
print(solution([1,2,3,4,5]))
print(solution([5,4,3,2,1]))
print(solution([6,1,1,1,1,1]))
print(solution([1,6,9,5,3,2,7]))

# 이 문제를 풀 때 여러 차례 실수를 했는데
# 기본적으로 인덱스 i를 stack에 append해주지 않는 실수와
# if prices[stack[-1]] > prices[i]: 로 안하고 stack을 처음 인덱스부터 순서대로 비교한 실수를 했다.
# 또한 stack이 비어있는 경우 넘어가지 않는 실수도 했기에 항상 이런 사소한 실수를 염두에 두어야겠다.