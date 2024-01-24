def solution(genres, plays):

    genre_table = {}
    play_table = {}
    length = len(genres)
    
    # genre별 play 횟수 스택한 table 생성
    for i in range(length):

        if genres[i] in play_table:
            play_table[genres[i]] += plays[i]
            genre_table[genres[i]].append((i, plays[i]))
        else:
            play_table[genres[i]] = plays[i]
            genre_table[genres[i]] = [(i, plays[i])]

    # play 횟수가 많은 genre 순으로 정렬
    play_sorted_genres = sorted(play_table.items(), key = lambda x: x[1], reverse = True)
    answer = []
    
    # play 횟수 합으로 정렬된 genre를 돌면서 해당 genre 내에서 play 횟수로 index 순서를 내림차순으로 정렬
    for genre, _ in play_sorted_genres:

        # 중요: 이런 식으로 lambda x: (-x[1], x[0])으로 해두면 x[1]을 기준으로 내림차순으로 정렬이 가능함.
        sorted_index_table = sorted(genre_table[genre], key = lambda x: (-x[1], x[0]))
        answer += [idx for idx, _ in sorted_index_table[:2]]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))