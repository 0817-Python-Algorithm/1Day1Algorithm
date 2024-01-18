def solution(want, number, discount):
    
    want_dic = {}
    answer = 0

    length = len(want)
    for i in range(length):
        want_dic[want[i]] = number[i]

    for start in range(len(discount) - 9):

        # Dictionary의 경우 A = B 이런 식으로 두면 깊은 복사가 되어버림.
        # 이걸 얕은 복사로 가져오는 방법이 copy 메소드임.
        # A = B.copy()와 같은 방식으로 하면 cbv로 가져올 수 있음.
        new_want_dic = want_dic.copy()
        for index in range(start, start+10):
            if discount[index] in new_want_dic:
                new_want_dic[discount[index]] -= 1
        
        # all(A for B)을 쓰면 B값들 중 A를 모두 만족하면 True를, 아니면 False를 return하게 코드를 짤 수 있음.
        # 이런 스킬을 가져간다면 마지막에 다시 한바퀴 돌면서 검색하는 코드 대신 간결하게 코드를 짤 수 있음.
        # 여기서는 어차피 new_want_dic의 길이만큼 돌기 때문에 want의 길이만큼만 돌게 됨.
        if all(value == 0 for value in new_want_dic.values()):
            answer += 1
    return answer

# want의 길이를 N, discount의 길이를 M이라고 하자.
# 이때 N은 아무리 길어봤자 최대 10이다.
# 그렇기에 시간복잡도가 O(N*M)이어도 결국엔 O(M)이 된다. 즉 O(N)이 되는 것이다.

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))