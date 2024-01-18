def solution(participant, completion):
    
    hash_table = {}
    
    for p in participant:
        if p in hash_table:
            hash_table[p] += 1
        else:
            hash_table[p] = 1
    
    for c in completion:
        hash_table[c] -= 1
        
    for k in hash_table.keys():
        if hash_table[k] > 0:
            return k
        
# 이런 식으로 하면 이전 풀이보다 조금 더 for문을 짧게 여러번 가져가면서 코드도 간결하게 보인다.

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))