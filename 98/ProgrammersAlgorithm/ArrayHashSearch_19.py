def hashing(list):
    p = 31
    m = 1_000_000_007
    
    hashed_list = []

    for s in list:
        hash_result = 0
        length = len(s)
        for i in range(length):
            # 여기서 ord 함수가 중요함. ord 함수는 인자로 들어온 char타입의 값을 유니코드로 변환해 줌.
            hash_result += (ord(s[i]) * p**i)%m
        hash_result %= m
        hashed_list.append(hash_result)
    return hashed_list

def solution(string_list, query_list):
    answer = []
    hashed_string_list = hashing(string_list)
    hashed_query_list = hashing(query_list)
    for query in hashed_query_list:
        # 해당 값이 배열에 포함되어 있는지를 확인하려면 in을 적극적으로 쓰자.
        # in 연산자를 좀 더 깊이 알아보자.
        # in은 리스트, 튜플에서는 하나씩 다 돌면서 확인해야 하기 때문에 O(N)의 시간복잡도를 갖는다.
        # 반면, Set, Dictionary에서는 내부적인 hash를 통해서 접근하기 때문에 시간복잡도가 O(1)이 가능하다.
        # 만약 충돌이 많이 발생할 경우엔 O(N)까지 떨어질 수도 있다.
        if query in hashed_string_list:
            answer.append(True)
        else:
            answer.append(False)
    return answer

print(solution(["apple", "banana", "cherry"], ["banana","kiwi"]))
print(solution(["apple", "banana", "cherry"], ["banana","kiwi","melon","apple"]))
