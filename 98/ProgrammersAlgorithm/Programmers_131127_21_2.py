# 이 방식은 해시 테이블에서 차감해나가는 방식이 아니라 
# 새로운 해시 테이블을 거꾸로 만들어나간 후 원래의 해시 테이블과 비교하는 방식이다.
def solution(want, number, discount):

    answer = 0

    want_dic = {}
    length = len(want)
    
    for i in range(length):
        want_dic[want[i]] = number[i]
    
    for start in range(0, len(discount)-9):
        new_want_dic = {}
        for index in range(start, start+10):
            if discount[index] in new_want_dic:
                new_want_dic[discount[index]] += 1
            else:
                new_want_dic[discount[index]] = 1
        if new_want_dic == want_dic:
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))