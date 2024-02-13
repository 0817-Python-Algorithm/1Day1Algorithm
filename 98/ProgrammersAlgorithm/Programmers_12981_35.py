def solution(n, words):
    
    # 각 사람별로 부른 단어를 저장하는 2차원 문자열 배열
    person = [[] for _ in range(n)]

    # 처음 사람은 뭘 불러도 상관 없으니 단어를 하나 넣어줌.
    person[0].append(words[0])

    # 불러진 단어들을 저장하는 문자열 배열
    used_word_list = [words[0]]
    
    for i in range(1, len(words)):
        
        # 앞사람이 부른 단어의 끝이랑 내가 부른 단어의 처음이 다를 경우
        if person[i % n - 1][-1][-1] != words[i][0]:
            return [i % n + 1, len(person[i % n]) + 1]
        
        # 내가 부른 단어가 이미 앞서 불러진 중복된 단어일 경우
        elif words[i] in used_word_list:
            return [i % n + 1, len(person[i % n]) + 1]
        
        # 올바르게 부른 단어의 경우는 자기 자신의 index의 person에 추가하고, 불러진 단어 목록에 추가
        else:
            person[i % n].append(words[i])
            used_word_list.append(words[i])
    
    return [0, 0]
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))