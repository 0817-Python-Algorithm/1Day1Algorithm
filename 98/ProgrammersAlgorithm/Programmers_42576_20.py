def solution(participant, completion):
    
    # Dictionary 타입은 참고로 모든 주요 내장 메소드의 시간복잡도가 O(1)이다.
    hash_table = {}

    for c in completion:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1

    answer = ""

    for p in participant:
        if hash_table.get(p) == None or hash_table.get(p) == 0:
            answer = p
            break
        else:
            hash_table[p] -= 1
    
    return answer
# 이렇게 하면 시간 복잡도가 O(N)이다. 큰 문제는 없지만 생각보다 코드에서 if문이 길다는 점이 조금 더러워보이긴 한다.
# 조금 더 간결하게 바꿀 수 있을 것 같다.

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))