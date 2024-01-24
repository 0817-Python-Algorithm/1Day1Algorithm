def solution(record):

    hash_table = {}

    for r in record:
        command = r.split()
        
        # 길이가 3이라면 명령어가 Enter이거나 Change 중 하나임.
        if len(command) == 3:
            hash_table[command[1]] = command[2] 
            
    answer = []
    
    # 모든 정리가 끝난 id-nickname 테이블(hash_table)을 기준으로 command 내역들을 순서대로 출력함.
    for r in record:
        line = r.split()
        command = line[0]
        id = line[1]

        if command == "Enter":
            answer.append(f"{hash_table.get(id)}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{hash_table.get(id)}님이 나갔습니다.")
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))